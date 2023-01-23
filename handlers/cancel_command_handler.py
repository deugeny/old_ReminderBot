import re
from typing import Union, Never

from messages import ERROR_MESSAGE, REQUEST_CANCELLATION_TARGET_MESSAGE
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from messages import UNKNOWN_JOB_FORMAT, ALL_JOBS_CANCELED
from apscheduler.jobstores.base import JobLookupError
from scheduler import scheduler
from bot import bot
from CurrentState import CurrentState
from callbacks.filters import cancel_remind_id

CANCEL_COMMAND_PATTERN = r'^\/cancel\s+(all)|(\d+)$'


class CancelHandler:
    def __init__(self, bot: AsyncTeleBot, scheduler: AsyncIOScheduler):
        assert bot is not None
        assert scheduler is not None
        self.__scheduler = scheduler
        self.__bot = bot
        self.__register_bot_handlers()

    async def cancel(self, cancellation_target: str, message: types.Message) -> Never:
        if cancellation_target is None:
            await self.__try_request_from_user_cancellation_target(message)
            return

        if cancellation_target == 'all':
            await self.__cancel_all_remind(message)
            return

        await self.__cancel_remind_by_id(cancellation_target, message)

    def __register_bot_handlers(self) -> Never:
        self.__bot.register_message_handler(commands=["cancel"], callback=self.__cancel_command_handle)
        self.__bot.register_message_handler(state=CurrentState.wait_cancel_data,
                                            callback=self.__cancel_handler_input_data)
        # noinspection PyTypeChecker
        self.__bot.register_callback_query_handler(self.__cancel_remind_callback, func=None,
                                                   parse_prefix=cancel_remind_id.filter())

    async def __cancel_command_handle(self, message: types.Message) -> Never:
        cancellation_target = parse_cancel_command(message.text)
        await self.cancel(cancellation_target, message)

    async def __cancel_handler_input_data(self, message: types.Message) -> Never:
        await self.cancel(message.text, message)

    async def __try_request_from_user_cancellation_target(self, message: types.Message) -> Never:
        try:
            await self.__bot.send_message(message.chat.id, REQUEST_CANCELLATION_TARGET_MESSAGE)
            await self.__bot.set_state(message.from_user.id, CurrentState.wait_cancel_data, message.chat.id)
        except Exception as e:
            await self.__bot.delete_state(message.from_user.id, message.chat.id)
            await self.__bot.reply_to(message, ERROR_MESSAGE)

    async def __cancel_remind_by_id(self, remind_id: str, message: types.Message) -> Never:
        try:
            self.__scheduler.remove_job(job_id=remind_id)
        except JobLookupError:
            await self.__bot.reply_to(message, UNKNOWN_JOB_FORMAT.format(remind_id))
        finally:
            await self.__bot.delete_state(message.from_user.id, message.chat.id)

    async def __cancel_all_remind(self, message: types.Message) -> Never:
        try:
            self.__scheduler.remove_all_jobs()
            await self.__bot.reply_to(message, ALL_JOBS_CANCELED)
            await self.__bot.delete_state(message.from_user.id, message.chat.id)
        finally:
            await self.__bot.delete_state(message.from_user.id, message.chat.id)

    async def __cancel_remind_callback(self, call: types.CallbackQuery) -> Never:
        data: dict = cancel_remind_id.parse(callback_data=call.data)
        remind_id = data.get('id')
        await self.cancel(remind_id, call.message)


def parse_cancel_command(text: str) -> str | None:
    match = re.search(CANCEL_COMMAND_PATTERN, text, flags=re.IGNORECASE)
    return match[match.lastindex] if match else None


cancel_handler: CancelHandler = CancelHandler(bot, scheduler)
