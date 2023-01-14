from telebot import types

from callbacks.filters import help_id, HELP_REMIND_ID, HELP_CANCEL_ID, HELP_HELP_ID, cancel_remind_id

HELP_CANCEL_COMMAND_BUTTON = 'help для cancel'
HELP_HELP_COMMAND_BUTTON = 'help для help'
HELP_REMIND_COMMAND_BUTTON = 'help для remind'
CANCEL_BUTTON_CAPTION = "Отменить"


async def create_help_buttons():
    help_markup = types.InlineKeyboardMarkup()
    help_markup.row(create_help_button(),  create_cancel_help_button(), create_remind_help_button())
    return help_markup


def create_remind_help_button():
    return types.InlineKeyboardButton(HELP_REMIND_COMMAND_BUTTON,
                                      callback_data=help_id.new(id=HELP_REMIND_ID))


def create_cancel_help_button():
    return types.InlineKeyboardButton(HELP_CANCEL_COMMAND_BUTTON,
                                      callback_data=help_id.new(id=HELP_CANCEL_ID))


def create_help_button():
    return types.InlineKeyboardButton(HELP_HELP_COMMAND_BUTTON, callback_data=help_id.new(id=HELP_HELP_ID))


def create_cancel_button(message_id):
    return types.InlineKeyboardButton(CANCEL_BUTTON_CAPTION, callback_data=cancel_remind_id.new(id=message_id))
