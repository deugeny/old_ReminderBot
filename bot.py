import telebot

import config
import messages

bot = telebot.TeleBot(config.API_TOKEN)
commands = [
    telebot.types.BotCommand("help", messages.HELP_COMMAND_DESCRIPTION),
    telebot.types.BotCommand("remind", messages.REMIND_COMMAND_DESCRIPTION),
    telebot.types.BotCommand("cancel", messages.CANCEL_COMMAND_DESCRIPTION),
]


def send_message(tbot, chat_id, text):
    tbot.send_message(chat_id, text)


bot.set_my_commands(commands=commands)
bot.polling(none_stop=True, interval=0)
