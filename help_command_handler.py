import re
import messages

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
    await bot.reply_to(message, messages.REMIND_MESSAGE)


async def send_help_for_help(bot, message):
    await bot.reply_to(message, messages.HELP_MESSAGE)


async def send_help_for_cancel(bot, message):
    await bot.reply_to(message, messages.CANCEL_MESSAGE)
