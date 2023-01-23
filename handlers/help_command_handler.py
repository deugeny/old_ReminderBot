import re
from typing import Union, Never

import messages
from telebot.async_telebot import AsyncTeleBot
from telebot import types

from HelpButtonsMarkup import HelpButtonsMarkup

HELP_COMMAND_PATTERN = r'^\/help\s+[\/]*(remind|cancel|help)$'

HELP_MESSAGES = {
    "/cancel": messages.CANCEL_MESSAGE,
    "/help": messages.HELP_MESSAGE,
    '/remind': messages.REMIND_MESSAGE
}


async def send_help(bot: AsyncTeleBot, message: types.Message) -> Never:
    command = parse_help_command(message.text)
    help_message_text = HELP_MESSAGES.get(command)
    if help_message_text is not None:
        await send_help_message(bot, message.chat.id, help_message_text)


def parse_help_command(text: str) -> str:
    match = re.search(HELP_COMMAND_PATTERN, text, flags=re.IGNORECASE)
    command = match[match.lastindex] if match else '/help'
    if not command.startswith('/'):
        command = '/' + command

    return command.lower()


async def send_help_message(bot: AsyncTeleBot, chat_id: Union[int, str], help_message_text: str) -> Never:
    markup = HelpButtonsMarkup()
    await bot.send_message(chat_id, help_message_text, parse_mode="markdown", reply_markup=markup)
