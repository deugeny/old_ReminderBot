import re
import messages

from buttons import create_help_buttons

HELP_COMMAND_PATTERN = r'^\/help\s+[\/]*(remind|cancel|help)$'


async def send_help(bot, message):
    command = parse_help_command(message.text)

    if command == '/cancel':
        await send_help_for_cancel(bot, message)

    if command == '/help':
        await send_help_for_help(bot, message)

    if command == '/remind':
        await send_help_for_remind(bot, message)


def parse_help_command(text):
    match = re.search(HELP_COMMAND_PATTERN, text)
    command = match[match.lastindex] if match else '/help'
    if not command.startswith('/'):
        command = '/' + command

    return command


async def send_help_for_remind(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.REMIND_MESSAGE, parse_mode="markdown", reply_markup=markup)


async def send_help_for_help(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.HELP_MESSAGE, parse_mode="markdown", reply_markup=markup)


async def send_help_for_cancel(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.CANCEL_MESSAGE, parse_mode="markdown", reply_markup=markup)
