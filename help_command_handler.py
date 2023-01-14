import re
import messages
from telebot import types
from filters import help_id, HELP_HELP_ID, HELP_CANCEL_ID, HELP_REMIND_ID

HELP_COMMAND_PATTERN = r'^\/help\s+[\/]*(remind|cancel|help)$'
HELP_CANCEL_COMMAND_BUTTON = 'help для cancel'
HELP_HELP_COMMAND_BUTTON = 'help для help'
HELP_REMIND_COMMAND_BUTTON = 'help для remind'


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


async def create_help_buttons():
    help_markup = types.InlineKeyboardMarkup()
    # help_markup.row(types.InlineKeyboardButton(HELP_HELP_COMMAND_BUTTON,
    #                                            callback_data=help_id.new(id=HELP_HELP_ID)))
    # help_markup.row(types.InlineKeyboardButton(HELP_CANCEL_COMMAND_BUTTON,
    #                                            callback_data=help_id.new(id=HELP_CANCEL_ID)))
    # help_markup.row(types.InlineKeyboardButton(HELP_REMIND_COMMAND_BUTTON,
    #                                            callback_data=help_id.new(id=HELP_REMIND_ID)))

    help_markup.row(types.InlineKeyboardButton(HELP_HELP_COMMAND_BUTTON, callback_data=help_id.new(id=HELP_HELP_ID)),
                     types.InlineKeyboardButton(HELP_CANCEL_COMMAND_BUTTON,
                                                callback_data=help_id.new(id=HELP_CANCEL_ID)),
                     types.InlineKeyboardButton(HELP_REMIND_COMMAND_BUTTON,
                                                callback_data=help_id.new(id=HELP_REMIND_ID)))

    return help_markup


async def send_help_for_remind(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.REMIND_MESSAGE, parse_mode="markdown", reply_markup=markup)


async def send_help_for_help(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.HELP_MESSAGE, parse_mode="markdown", reply_markup=markup)


async def send_help_for_cancel(bot, message):
    markup = await create_help_buttons()
    await bot.reply_to(message, messages.CANCEL_MESSAGE, parse_mode="markdown", reply_markup=markup)
