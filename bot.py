import asyncio
from typing import Union

from telebot.async_telebot import AsyncTeleBot
from telebot import types, asyncio_filters
from telebot.asyncio_storage import StateMemoryStorage

from callbacks.filters import ParsePrefix, cancel_remind_id, help_id
import config
import messages
from callbacks.help_callback import help_callback

bot = AsyncTeleBot(config.API_TOKEN, state_storage=StateMemoryStorage())

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
    bot.register_callback_query_handler(help_callback, pass_bot=True, func=None,
                                        parse_prefix=help_id.filter())


async def init_bot() -> None:
    await register_filters(bot)
    register_callback_handlers(bot)
    await init_bot_commands(bot)
    await asyncio.gather(bot.polling())


async def register_filters(bot: AsyncTeleBot) -> None:
    bot.add_custom_filter(asyncio_filters.StateFilter(bot))
    bot.add_custom_filter(asyncio_filters.IsDigitFilter())
