import messages
from bot import bot


@bot.message_handler(commands=['remind'])
def remind_handler(message):
    bot.reply_to(message, messages.REMIND_MESSAGE)


@bot.message_handler(commands=['cancel'])
def remind_handler(message):
    pass


@bot.message_handler(commands=['help'])
def start_handler(message):
    bot.reply_to(message, messages.HELP_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*remind$")
def handle_help_remind_message(message):
    bot.reply_to(messages.REMIND_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*help$")
def handle_help_help_message(message):
    bot.reply_to(messages.HELP_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*cancel$")
def handle_help_cancel_message(message):
    bot.reply_to(messages.CANCEL_MESSAGE)
