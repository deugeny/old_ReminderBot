from telebot.custom_filters import SimpleCustomFilter
from telebot import types, AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter


# class AdminFilter(SimpleCustomFilter):
#     key = 'admin'
#     def check(self, message):
#         return int(message.from_user.id) in ADMIN

class ParsePrefix(AdvancedCustomFilter):
    key = 'parse_prefix'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


cancel_remind_id = CallbackData("id", prefix="cancel_remind")
