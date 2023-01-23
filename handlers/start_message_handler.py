from messages import START_MESSAGE
from StartMessageMarkup import StartMessageMarkup


async def send_start_message(bot, message):
    markup = StartMessageMarkup()
    await bot.send_message(message.chat.id, START_MESSAGE, parse_mode='html',
                           reply_markup=markup)
