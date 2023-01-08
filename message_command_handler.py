import re
from datetime import datetime

import messages
from scheduler import is_valid_start_datetime
from bot import send_message
import datefinder

from config import DATE_FIRST_PART_KIND
from messages import ERROR_DATETIME, CONFIRMATION_MESSAGE

REMIND_COMMANDS = ('/remind',)

# trouble ticket number regular expression pattern
TROUBLE_TICKET_NUMBER_PATTERN = r'\d{8}'


def schedule_remind(bot, scheduler, message):
    (start_at, text, trouble_ticket) = parse_remind_message(message.text)
    if not is_valid_start_datetime(start_at):
        bot.reply_to(message, ERROR_DATETIME)
        bot.reply_to(message, messages.REMIND_MESSAGE)
        return False
    scheduler.add_job(send_message, 'date', run_date=start_at, id=str(message.id), args=[message.chat.id, text])
    cancel_message = CONFIRMATION_MESSAGE.format(start_at, message.id)
    bot.reply_to(message, cancel_message)
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
    start_at = try_get_datetime_from_message(text, base_date=datetime.today())
    trouble_ticket = try_get_trouble_ticket_number(text)
    return start_at, text, trouble_ticket


def try_get_trouble_ticket_number(text):
    numbers_match = re.search(TROUBLE_TICKET_NUMBER_PATTERN, text)
    return numbers_match[0] if numbers_match else None


def try_get_datetime_from_message(text, base_date=None):
    dates = list(datefinder.find_dates(text, first=DATE_FIRST_PART_KIND, base_date=base_date))
    return dates[0] if len(dates) > 0 else None
