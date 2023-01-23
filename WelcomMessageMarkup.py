from typing import Never, Final

from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks.filters import help_id, HELP_COMMAND_ID, SHOW_COMMAND_ID, REMIND_COMMAND_ID, command_id, \
    CANCEL_COMMAND_ID


class WelcomeMessageMarkup(InlineKeyboardMarkup):
    __REMIND_COMMAND_BUTTON: Final = "⏰ создать"
    __HELP_COMMAND_BUTTON: Final = "❔помощь"
    __SHOW_COMMAND_BUTTON: Final = "🔍 просмотр"
    __CANCEL_COMMAND_BUTTON: Final = "❌ отменить"

    def __init__(self):
        super().__init__(keyboard=None, row_width=2)
        self.__create_sections_markup()

    def __create_sections_markup(self) -> Never:
        self.row(WelcomeMessageMarkup.__create_remind_button(), WelcomeMessageMarkup.__create_cancel_command_button())
        self.row(WelcomeMessageMarkup.__create_show_button(), WelcomeMessageMarkup.__create_help_button())

    @staticmethod
    def __create_help_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(WelcomeMessageMarkup.__HELP_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=HELP_COMMAND_ID))

    @staticmethod
    def __create_show_button(cls) -> InlineKeyboardButton:
        return types.InlineKeyboardButton(WelcomeMessageMarkup.__SHOW_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=SHOW_COMMAND_ID))

    @staticmethod
    def __create_remind_button(cls) -> InlineKeyboardButton:
        return types.InlineKeyboardButton(WelcomeMessageMarkup.__REMIND_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=REMIND_COMMAND_ID))

    @staticmethod
    def __create_cancel_command_button(cls) -> InlineKeyboardButton:
        return types.InlineKeyboardButton(WelcomeMessageMarkup.__CANCEL_COMMAND_BUTTON,
                                          callback_data=command_id.new(id=CANCEL_COMMAND_ID))
