import telebot

import config
import messages

bot = telebot.TeleBot(config.API_TOKEN)
commands = [
    telebot.types.BotCommand("help", messages.HELP_COMMAND_DESCRIPTION),
    telebot.types.BotCommand("remind", messages.REMIND_COMMAND_DESCRIPTION),
    telebot.types.BotCommand("cancel", messages.CANCEL_COMMAND_DESCRIPTION),
]

bot.set_my_commands(commands=commands)


def send_message(chat_id, text):
    bot.send_message(chat_id, text)
