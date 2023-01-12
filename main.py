from cancel_command_handler import cancel_reminders
from message_command_handler import schedule_remind
from welcome_message_handler import send_welcome_message
from cancel_callback import cancel_remind_callback
from filters import cancel_remind_id
from help_command_handler import send_help
from scheduler import scheduler
from bot import bot, init_bot_commands
import asyncio


@bot.message_handler(commands=['start'])
async def remind_handler(message):
    await send_welcome_message(bot, message)


@bot.message_handler(commands=['remind'])
async def remind_handler(message):
    await schedule_remind(bot, scheduler, message)


@bot.message_handler(commands=['cancel'])
async def cancel_handler(message):
    await cancel_reminders(bot, scheduler, message)


@bot.message_handler(commands=['help'])
async def start_handler(message):
    await send_help(bot, message)


async def main():
    scheduler.start()
    bot.register_callback_query_handler(cancel_remind_callback, func=None, pass_bot=True,
                                        parse_prefix=cancel_remind_id.filter())

    await init_bot_commands(bot)
    await asyncio.gather(bot.polling())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
