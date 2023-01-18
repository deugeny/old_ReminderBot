from handlers.cancel_command_handler import cancel_handler, parse_cancel_command
from handlers.remind_command_handler import schedule_remind
from handlers.welcome_message_handler import send_welcome_message
from handlers.help_command_handler import send_help
from scheduler import scheduler
from bot import bot, init_bot
from CurrentState import CurrentState
import asyncio


@bot.message_handler(commands=['start'])
async def remind_handler(message):
    await send_welcome_message(bot, message)


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
