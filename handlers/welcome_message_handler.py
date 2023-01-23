from messages import WELCOME_MESSAGE
from WelcomMessageMarkup import WelcomeMessageMarkup
from telebot import formatting


async def send_welcome_message(bot, message):
    markup = WelcomeMessageMarkup()
    await bot.send_message(message.chat.id, formatting.format_text(WELCOME_MESSAGE), parse_mode='html',
                           reply_markup=markup)
