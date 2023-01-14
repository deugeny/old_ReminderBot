from messages import WELCOME_MESSAGE
from buttons import create_help_buttons


async def send_welcome_message(bot, message):
    markup = create_help_buttons()
    await bot.send_message(message.chat.id, WELCOME_MESSAGE, parse_mode='markdown', reply_markup=markup)
