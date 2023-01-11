from bot import bot
from telebot import types, TeleBot
from filters import cancel_remind_id
from scheduler import scheduler
from cancel_command_handler import cancel_remind


def cancel_remind_callback(call: types.CallbackQuery, bot: TeleBot):
    data: dict = cancel_remind_id.parse(callback_data=call.data)
    remind_id = data.get('id')
    cancel_remind(bot, scheduler, remind_id, call.message)


bot.register_callback_query_handler(cancel_remind_callback, func=None, pass_bot=True,
                                    parse_prefix=cancel_remind_id.filter())
