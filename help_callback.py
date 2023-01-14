from telebot.async_telebot import AsyncTeleBot
from telebot import types
from filters import help_id, HELP_REMIND_ID, HELP_CANCEL_ID, HELP_HELP_ID
from help_command_handler import send_help_for_help, send_help_for_remind, send_help_for_cancel, send_help


async def help_callback(call: types.CallbackQuery, bot: AsyncTeleBot):
    data: dict = help_id.parse(callback_data=call.data)
    help_target = data.get('id')

    if help_target == HELP_CANCEL_ID:
        await send_help_for_cancel(bot, call.message)
        return

    if help_target == HELP_REMIND_ID:
        await send_help_for_remind(bot, call.message)
        return

    await send_help_for_help(bot, call.message)
