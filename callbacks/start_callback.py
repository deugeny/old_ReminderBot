from telebot.async_telebot import AsyncTeleBot
from telebot import types
from callbacks.filters import command_id, REMIND_COMMAND_ID
from handlers import remind_command_handler
from handlers.help_command_handler import send_help

async def start_callback(call: types.CallbackQuery, bot: AsyncTeleBot):
    data: dict = command_id.parse(callback_data=call.data)
    command_target = data.get('id')
    if command_target == REMIND_COMMAND_ID:
        await remind_command_handler.remind_handler.schedule_remind(call.message)

    # help_command = HELP_COMMANDS.get(help_target)
    # if help_command is None:
    #     help_command = "/help help"
    #
    # message = call.message
    # message.text = help_command
    # await send_help(bot, message)
