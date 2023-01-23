from telebot.asyncio_filters import types, AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter

HELP_REMIND_ID = 'help_remind'
HELP_CANCEL_ID = 'help_cancel'
HELP_HELP_ID = 'help_help'

REMIND_COMMAND_ID = 'remind_command'
HELP_COMMAND_ID = 'help_command'
CANCEL_COMMAND_ID = 'cancel_command'
SHOW_COMMAND_ID = 'show_command'
START_COMMAND_ID = 'start_command'


# class AdminFilter(SimpleCustomFilter):
#     key = 'admin'
#     def check(self, message):
#         return int(message.from_user.id) in ADMIN

class ParsePrefix(AdvancedCustomFilter):
    key = 'parse_prefix'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


cancel_remind_id = CallbackData("id", prefix="cancel_remind")
help_id = CallbackData("id", prefix="help")
command_id = CallbackData("id", prefix="command_id")
