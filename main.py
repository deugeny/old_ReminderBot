from handlers.cancel_command_handler import cancel_reminders
from handlers.remind_command_handler import schedule_remind
from handlers.welcome_message_handler import send_welcome_message
from handlers.help_command_handler import send_help
from scheduler import scheduler
from bot import bot, init_bot_commands, register_callback_handlers
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
    register_callback_handlers(bot)

    await init_bot_commands(bot)
    await asyncio.gather(bot.polling())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
