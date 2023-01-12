from messages import WELCOME_MESSAGE


async def send_welcome_message(bot, message):
    await bot.send_message(message.chat.id, WELCOME_MESSAGE)
