import asyncio
from typing import Union

from telebot.async_telebot import AsyncTeleBot
from telebot import types

from callbacks.cancel_callback import cancel_remind_callback
from callbacks.filters import ParsePrefix, cancel_remind_id, help_id
import config
import messages
from callbacks.help_callback import help_callback

bot = AsyncTeleBot(config.API_TOKEN)

commands = [
    types.BotCommand("start", messages.HELP_COMMAND_DESCRIPTION),
    types.BotCommand("help", messages.HELP_COMMAND_DESCRIPTION),
    types.BotCommand("remind", messages.REMIND_COMMAND_DESCRIPTION),
    types.BotCommand("cancel", messages.CANCEL_COMMAND_DESCRIPTION),
]


async def init_bot_commands(bot: AsyncTeleBot) -> None:
    await bot.delete_my_commands(scope=None, language_code=None)
    await bot.set_my_commands(commands=commands, scope=None, language_code=None)

    bot.add_custom_filter(ParsePrefix())


async def send_message(chat_id: Union[int, str], text: str) -> None:
    await bot.send_message(chat_id, text)


def register_callback_handlers(bot: AsyncTeleBot) -> None:
    bot.register_callback_query_handler(cancel_remind_callback, func=None, pass_bot=True,
                                        parse_prefix=cancel_remind_id.filter())
    bot.register_callback_query_handler(help_callback, func=None, pass_bot=True,
                                        parse_prefix=help_id.filter())


async def init_bot():
    register_callback_handlers(bot)
    await init_bot_commands(bot)
    await asyncio.gather(bot.polling())
