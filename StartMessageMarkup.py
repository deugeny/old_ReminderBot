from typing import Never, Final

from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks.filters import help_id, HELP_COMMAND_ID, SHOW_COMMAND_ID, REMIND_COMMAND_ID, command_id, \
    CANCEL_COMMAND_ID


class StartMessageMarkup(InlineKeyboardMarkup):
    __REMIND_COMMAND_BUTTON: Final = "⏰ создать"
    __HELP_COMMAND_BUTTON: Final = "❔помощь"
    __SHOW_COMMAND_BUTTON: Final = "🔍 просмотр"
    __CANCEL_COMMAND_BUTTON: Final = "❌ отменить"

    def __init__(self):
        super().__init__(keyboard=None, row_width=2)
        self.__create_sections_markup()

    def __create_sections_markup(self) -> Never:
        self.row(StartMessageMarkup.__create_remind_button(), StartMessageMarkup.__create_cancel_command_button())
        self.row(StartMessageMarkup.__create_show_button(), StartMessageMarkup.__create_help_button())

    @staticmethod
    def __create_help_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(StartMessageMarkup.__HELP_COMMAND_BUTTON,
                                          callback_data=command_id.new(id=HELP_COMMAND_ID))

    @staticmethod
    def __create_show_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(StartMessageMarkup.__SHOW_COMMAND_BUTTON,
                                          callback_data=command_id.new(id=SHOW_COMMAND_ID))

    @staticmethod
    def __create_remind_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(StartMessageMarkup.__REMIND_COMMAND_BUTTON,
                                          callback_data=command_id.new(id=REMIND_COMMAND_ID))

    @staticmethod
    def __create_cancel_command_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(StartMessageMarkup.__CANCEL_COMMAND_BUTTON,
                                          callback_data=command_id.new(id=CANCEL_COMMAND_ID))
