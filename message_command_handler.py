import re
from datetime import datetime, date, time

import messages
from scheduler import is_valid_start_datetime
from bot import send_message
import datefinder
from telebot import types
from filters import cancel_remind_id

from config import DATE_FIRST_PART_KIND
from messages import ERROR_DATETIME, CONFIRMATION_MESSAGE

REMIND_COMMANDS = ('/remind',)

# trouble ticket number regular expression pattern
TROUBLE_TICKET_NUMBER_PATTERN = r'\d{8}'

ZERO_DATE: date = date.min
ZERO_TIME: time = time.min
DEFAULT_DATE: datetime = datetime.combine(date=ZERO_DATE, time=ZERO_TIME)


def schedule_remind(bot, scheduler, message):
    (start_at, text, trouble_ticket) = parse_remind_message(message.text)
    if not is_valid_start_datetime(start_at):
        bot.reply_to(message, ERROR_DATETIME)
        bot.reply_to(message, messages.REMIND_MESSAGE)
        return False
    scheduler.add_job(send_message, 'date', run_date=start_at, id=str(message.id), args=[message.chat.id, text])
    cancel_message = CONFIRMATION_MESSAGE.format(start_at, message.id)
    cancel_markup = types.InlineKeyboardMarkup()
    cancel_markup.row(types.InlineKeyboardButton("Cancel",
                                            callback_data=cancel_remind_id.new(id=message.id)))
    bot.reply_to(message, cancel_message, parse_mode="markdown", reply_markup=cancel_markup)
    return True


def parse_remind_message(message, commands=REMIND_COMMANDS):
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


def try_get_trouble_ticket_number(text):
    numbers_match = re.search(TROUBLE_TICKET_NUMBER_PATTERN, text)
    return numbers_match[0] if numbers_match else None


def try_get_datetime_from_message(text):
    datetime_from_text = list(datefinder.find_dates(text, first=DATE_FIRST_PART_KIND, base_date=DEFAULT_DATE))
    if len(datetime_from_text) == 0:
        return None

    candidate_date = None
    candidate_time = None

    for candidate in datetime_from_text:
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
