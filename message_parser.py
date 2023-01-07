import re
from datetime import datetime

import datefinder

from config import TROUBLE_TICKET_NUMBER_PATTERN, DATE_FIRST_PART_KIND

REMIND_COMMANDS = ('/remind',)

CANCEL_COMMAND_PATTERN = r'^\/cancel\s+(all)|(\d+)$'


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


def parse_cancel_command(text):
    match = re.search(CANCEL_COMMAND_PATTERN, text)
    return match[match.lastindex] if match else None
