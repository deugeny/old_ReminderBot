from telebot.async_telebot import AsyncTeleBot
from telebot import types
from callbacks.filters import cancel_remind_id
from handlers.cancel_command_handler import cancel_handler
from bot import bot


async def cancel_remind_callback(call: types.CallbackQuery, bot: AsyncTeleBot):
    data: dict = cancel_remind_id.parse(callback_data=call.data)
    remind_id = data.get('id')
    await cancel_handler.cancel(remind_id, call.message)


bot.register_callback_query_handler(cancel_remind_callback, pass_bot=True,
                                    parse_prefix=cancel_remind_id.filter())
