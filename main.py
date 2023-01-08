from cancel_command_handler import cancel_reminders
from message_command_handler import schedule_remind
import messages
from scheduler import scheduler
from bot import bot


@bot.message_handler(commands=['remind'])
def remind_handler(message):
    schedule_remind(bot, scheduler, message)


@bot.message_handler(commands=['cancel'])
def cancel_handler(message):
    return cancel_reminders(bot, scheduler, message)


@bot.message_handler(commands=['help'])
def start_handler(message):
    bot.reply_to(message, messages.HELP_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*remind$")
def handle_help_remind_message(message):
    bot.reply_to(message, messages.REMIND_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*help$")
def handle_help_help_message(message):
    bot.reply_to(message, messages.HELP_MESSAGE)


@bot.message_handler(regexp=r"^\/help\s+[\/]*cancel$")
def handle_help_cancel_message(message):
    bot.reply_to(message, messages.CANCEL_MESSAGE)
