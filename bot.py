from telebot.async_telebot import AsyncTeleBot
from telebot import types
from filters import ParsePrefix
import config
import messages

bot = AsyncTeleBot(config.API_TOKEN)

commands = [
        types.BotCommand("start", messages.HELP_COMMAND_DESCRIPTION),
        types.BotCommand("help", messages.HELP_COMMAND_DESCRIPTION),
        types.BotCommand("remind", messages.REMIND_COMMAND_DESCRIPTION),
        types.BotCommand("cancel all", messages.CANCEL_COMMAND_DESCRIPTION),
    ]


async def init_bot_commands(bot: AsyncTeleBot):
    await bot.delete_my_commands(scope=None, language_code=None)
    bot.set_my_commands(commands=commands)
    bot.add_custom_filter(ParsePrefix())


async def send_message(chat_id, text):
    await bot.send_message(chat_id, text)
