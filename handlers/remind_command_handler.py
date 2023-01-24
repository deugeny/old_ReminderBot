import re
from datetime import datetime, date, time
from typing import Union, Callable, Optional, Tuple, Iterator, Never

from CancelMarkup import CancelMarkup
from CurrentState import CurrentState
from HelpButtonsMarkup import HelpButtonsMarkup
from callbacks.filters import command_id, REMIND_COMMAND_ID
from scheduler import get_scheduler, is_valid_start_datetime
from bot import get_bot
import datefinder
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import DATE_FIRST_PART_KIND
from messages import ERROR_DATETIME, CONFIRMATION_MESSAGE

REMIND_COMMANDS = ('/remind',)

# trouble ticket number regular expression pattern
TROUBLE_TICKET_NUMBER_PATTERN = r'\d{8}'

ZERO_DATE: date = date.min
ZERO_TIME: time = time.min
DEFAULT_DATE: datetime = datetime.combine(date=ZERO_DATE, time=ZERO_TIME)


class ReminderHandler:
    def __init__(self, get_bot_func: Callable[[], AsyncTeleBot], get_scheduler_func: Callable[[], AsyncIOScheduler]):
        self.__get_scheduler = get_scheduler_func
        self.__get_bot = get_bot_func
        self.bot.register_message_handler(commands=['remind'], callback=self.__handle_remind)
        self.bot.register_edited_message_handler(commands=['remind'],
                                                 callback=self.__handle_remind_message_user_changing)
        self.bot.register_message_handler(state=CurrentState.wait_remind_data, func=None,
                                          callback=self.__handle_remind)
        self.bot.register_callback_query_handler(callback=self.__start_callback, pass_bot=False, func=None,
                                                 parse_prefix=command_id.filter(id='remind_command'))

    @property
    def bot(self) -> AsyncTeleBot:
        return self.__get_bot()

    @property
    def scheduler(self) -> AsyncIOScheduler:
        return self.__get_scheduler()

    async def send_message(self, chat_id: Union[int, str], text: str) -> Never:
        await self.bot.send_message(chat_id, text)

    async def __start_callback(self, call: types.CallbackQuery) -> Never:
        await self.schedule_remind("", call.from_user.id, call.message.chat.id)

    async def __handle_remind(self, message: types.Message) -> Never:
        await self.schedule_remind(message.text, message.from_user.id, message.chat.id, message.message_id)

    async def schedule_remind(self, text: str, user_id: int, chat_id, message_id: int | None = None) -> Never:
        await self.bot.delete_state(user_id, chat_id)
        (start_at, text, trouble_ticket) = parse_remind_message(text)
        if not is_valid_start_datetime(start_at):
            await self.bot.set_state(user_id, CurrentState.wait_remind_data, chat_id)
            await self.bot.send_message(chat_id, "введите сообщение")
            return

        if message_id is not None:
            self.scheduler.add_job(self.send_message, 'date', run_date=start_at, id=str(message_id),
                                   args=[chat_id, text])

            await self.__send_confirmation_message(chat_id, message_id, start_at)

    async def __handle_remind_message_user_changing(self, message: types.Message) -> Never:
        (start_at, text, trouble_ticket) = parse_remind_message(message.text)
        if not is_valid_start_datetime(start_at):
            help_markup = HelpButtonsMarkup(commands='/remind')
            await self.bot.reply_to(message, ERROR_DATETIME, parse_mode="markdown", reply_markup=help_markup)
            return

        self.scheduler.reschedule_job(self.send_message, 'date', run_date=start_at, id=str(message.id),
                                      args=[message.chat.id, text])

        await self.__send_confirmation_message(message.chat.id, message.message_id, start_at)
        return

    async def __send_confirmation_message(self, chat_id: int, message_id: int, start_at: datetime) -> Never:
        confirmation_message = CONFIRMATION_MESSAGE.format(start_at, message_id)
        cancel_markup = CancelMarkup(str(message_id))
        await self.bot.send_message(chat_id, confirmation_message, reply_to_message_id=message_id,
                                    parse_mode="markdown",
                                    reply_markup=cancel_markup)


remind_handler = ReminderHandler(get_bot, get_scheduler)


def parse_remind_message(message: str, commands: Optional[Iterator[str]] = REMIND_COMMANDS) -> Tuple[
    datetime | None, str | None, str | None]:
    """
    Осуществляет разбор сообщения указанного в параметре text.
    В тексте пытается обнаружить дату и время, а также номер инцидента (8 цифровых символов подряд)
    :param message:
        str - текст разбираемого сообщения.
    :param commands:
        итератор содержащий список названий команд которые будут удаления из текста сообщения.
    :return:
        Возвращает кортеж из трех элементов.
            start_at - дата и время из сообщения или None если данные не были найдены
            text - текст сообщения
            trouble_ticket -номер инцидента или None если данные не были найден
    """
    text = message
    for command in commands:
        text = text.replace(command, '')
    text = text.strip()
    start_at = try_get_datetime_from_message(text)
    trouble_ticket = try_get_trouble_ticket_number(text)
    return start_at, text, trouble_ticket


def try_get_trouble_ticket_number(text: str) -> str | None:
    numbers_match = re.search(TROUBLE_TICKET_NUMBER_PATTERN, text)
    return numbers_match[0] if numbers_match else None


def try_get_datetime_from_message(text: str) -> datetime | None:
    extracted_datetimes = list(datefinder.find_dates(text, first=DATE_FIRST_PART_KIND, base_date=DEFAULT_DATE))
    if len(extracted_datetimes) == 0:
        return None

    candidate_date = None
    candidate_time = None

    for candidate in extracted_datetimes:
        date_part = candidate.date()
        time_part = candidate.time()
        if date_part != ZERO_DATE and time_part != ZERO_TIME:
            return candidate

        if date_part == ZERO_DATE:
            candidate_time = time_part
        if time_part == ZERO_TIME:
            candidate_date = date_part

    if candidate_time is None:
        return None

    if candidate_date is None:
        candidate_date = datetime.today().date()

    return datetime.combine(candidate_date, candidate_time)
