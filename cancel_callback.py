from telebot.async_telebot import AsyncTeleBot
from telebot import types
from filters import cancel_remind_id
from scheduler import scheduler
from cancel_command_handler import cancel_remind


async def cancel_remind_callback(call: types.CallbackQuery, bot: AsyncTeleBot):
    data: dict = cancel_remind_id.parse(callback_data=call.data)
    remind_id = data.get('id')
    await cancel_remind(bot, scheduler, remind_id, call.message)
