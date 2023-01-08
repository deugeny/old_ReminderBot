import cancel_command_handler
import message_parser
import messages
from messages import UNKNOWN_JOB_FORMAT, ALL_JOBS_CANCELED
from scheduler import scheduler
from bot import bot
from apscheduler.jobstores.base import JobLookupError


@bot.message_handler(commands=['remind'])
def remind_handler(message):
    bot.reply_to(message, messages.REMIND_MESSAGE)


@bot.message_handler(commands=['cancel'])
def cancel_handler(message):
    cancellation_target = cancel_command_handler.parse_cancel_command(message.text)
    invalid_cancellation_target = cancellation_target is None
    if invalid_cancellation_target:
        bot.reply_to(messages.INVALID_ARGUMENT + messages.CANCEL_MESSAGE)
        return False

    cancel_all_reminders = cancellation_target == 'all'
    if cancel_all_reminders:
        scheduler.remove_all_jobs()
        bot.reply_to(ALL_JOBS_CANCELED)
        return True

    try:
        scheduler.remove_job(job_id=cancellation_target)
        return True
    except JobLookupError:
        bot.reply_to(format(UNKNOWN_JOB_FORMAT, cancellation_target))

    return False


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
