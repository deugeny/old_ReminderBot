import re
import messages
from messages import UNKNOWN_JOB_FORMAT, ALL_JOBS_CANCELED
from apscheduler.jobstores.base import JobLookupError


CANCEL_COMMAND_PATTERN = r'^\/cancel\s+(all)|(\d+)$'


async def cancel_reminders(bot, scheduler, message):
    cancellation_target = parse_cancel_command(message.text)
    if cancellation_target is None:
        return await send_error_message(bot, message)

    if cancellation_target == 'all':
        return await cancel_all_remind(bot, scheduler, message)

    return await cancel_remind(bot, scheduler, cancellation_target, message)


async def send_error_message(bot, message):
    await bot.reply_to(message, messages.INVALID_ARGUMENT + messages.CANCEL_MESSAGE)
    return False


async def cancel_remind(bot, scheduler, remind_id, message):
    try:
        scheduler.remove_job(job_id=remind_id)
        return True
    except JobLookupError:
        await bot.reply_to(message, UNKNOWN_JOB_FORMAT.format(remind_id))
    return False


async def cancel_all_remind(bot, scheduler, message):
    scheduler.remove_all_jobs()
    await bot.reply_to(message, ALL_JOBS_CANCELED)
    return True


def parse_cancel_command(text):
    match = re.search(CANCEL_COMMAND_PATTERN, text)
    return match[match.lastindex] if match else None



