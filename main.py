from cancel_command_handler import cancel_reminders
from message_command_handler import schedule_remind
from help_command_handler import send_help
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
    send_help(bot, message)


if __name__ == '__main__':
    scheduler.start()
    bot.infinity_polling(none_stop=True, interval=0)
