import re
from typing import Union

import messages
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from messages import UNKNOWN_JOB_FORMAT, ALL_JOBS_CANCELED
from apscheduler.jobstores.base import JobLookupError
from scheduler import scheduler
from bot import bot
from CurrentState import CurrentState

ERROR_MESSAGE = "Произошла ошибка"

REQUEST_CANCELLATION_TARGET_MESSAGE = 'Укажите номер отменяемого задания или all для отмены всех заданий?'

CANCEL_COMMAND_PATTERN = r'^\/cancel\s+(all)|(\d+)$'


class CancelHandler:
    def __init__(self, bot: AsyncTeleBot, scheduler: AsyncIOScheduler):
        assert bot is not None
        assert scheduler is not None
        self.scheduler = scheduler
        self.bot = bot
        self.__register_message_handlers()

    def __register_message_handlers(self):
        self.bot.register_message_handler(commands=["cancel"], callback=self.__cancel_command_handle)
        self.bot.register_message_handler(state=CurrentState.wait_cancel_data,
                                          callback=self.__cancel_handler_input_data)

    async def cancel(self, cancellation_target: str, message: types.Message) -> bool | None:
        if cancellation_target is None:
            await self.__try_request_from_user_cancellation_target(message)
            return

        if cancellation_target == 'all':
            await self.__cancel_all_remind(message)
            return

        await self.__cancel_remind_by_id(cancellation_target, message)

    async def __cancel_command_handle(self, message: types.Message) -> None:
        cancellation_target = parse_cancel_command(message.text)
        await cancel_handler.cancel(cancellation_target, message)

    async def __cancel_handler_input_data(self, message: types.Message) -> None:
        await cancel_handler.cancel(message.text, message)

    async def __try_request_from_user_cancellation_target(self, message: types.Message) -> None:
        try:
            await self.bot.send_message(message.chat.id, REQUEST_CANCELLATION_TARGET_MESSAGE)
            await self.bot.set_state(message.from_user.id, CurrentState.wait_cancel_data, message.chat.id)
        except Exception as e:
            await self.bot.delete_state(message.from_user.id, message.chat.id)
            await self.bot.reply_to(message, ERROR_MESSAGE)

    async def __cancel_remind_by_id(self, remind_id: str, message: types.Message) -> None:
        try:
            self.scheduler.remove_job(job_id=remind_id)
        except JobLookupError:
            await self.bot.reply_to(message, UNKNOWN_JOB_FORMAT.format(remind_id))
        finally:
            await self.bot.delete_state(message.from_user.id, message.chat.id)

    async def __cancel_all_remind(self, message: types.Message) -> None:
        try:
            self.scheduler.remove_all_jobs()
            await self.bot.reply_to(message, ALL_JOBS_CANCELED)
            await self.bot.delete_state(message.from_user.id, message.chat.id)
        finally:
            await self.bot.delete_state(message.from_user.id, message.chat.id)


def parse_cancel_command(text: str) -> Union[str, None]:
    match = re.search(CANCEL_COMMAND_PATTERN, text, flags=re.IGNORECASE)
    return match[match.lastindex] if match else None


cancel_handler: CancelHandler = CancelHandler(bot, scheduler)
