from handlers.start_message_handler import send_start_message
from handlers.help_command_handler import send_help
from scheduler import scheduler
from handlers.remind_command_handler import remind_handler
from handlers.cancel_command_handler import cancel_handler
from bot import bot, init_bot
import asyncio


@bot.message_handler(commands=['start'])
async def remind_handler(message):
    await send_start_message(bot, message)


@bot.message_handler(commands=['help'])
async def start_handler(message):
    await send_help(bot, message)


async def main():
    scheduler.start()
    await init_bot()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
