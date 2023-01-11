from messages import WELCOME_MESSAGE

def send_welcome_message(bot, message):
    bot.send_message(message.chat.id, WELCOME_MESSAGE)