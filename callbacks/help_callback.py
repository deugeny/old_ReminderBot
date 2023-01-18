from telebot.async_telebot import AsyncTeleBot
from telebot import types
from callbacks.filters import help_id, HELP_REMIND_ID, HELP_CANCEL_ID, HELP_HELP_ID
from handlers.help_command_handler import send_help

HELP_COMMANDS = {
    HELP_CANCEL_ID: "/help cancel",
    HELP_REMIND_ID: "/help remind",
    HELP_HELP_ID: "/help help",
}


async def help_callback(call: types.CallbackQuery, bot: AsyncTeleBot):
    data: dict = help_id.parse(callback_data=call.data)
    help_target = data.get('id')
    help_command = HELP_COMMANDS.get(help_target)
    if help_command is None:
        help_command = "/help help"
    
    message = call.message
    message.text = help_command
    await send_help(bot, message)
