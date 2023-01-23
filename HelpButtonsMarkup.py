from typing import Final

from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks.filters import help_id, HELP_REMIND_ID, HELP_CANCEL_ID, HELP_HELP_ID


class HelpButtonsMarkup(InlineKeyboardMarkup):
    __HELP_CANCEL_COMMAND_BUTTON: Final = 'help для cancel'
    __HELP_HELP_COMMAND_BUTTON: Final = 'help для help'
    __HELP_REMIND_COMMAND_BUTTON: Final = 'help для remind'

    def create_help_buttons(self):
        self.row(HelpButtonsMarkup.__create_help_help_button(),
                 HelpButtonsMarkup.__create_cancel_help_button(),
                 HelpButtonsMarkup.__create_remind_help_button())

    @staticmethod
    def __create_remind_help_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(HelpButtonsMarkup.__HELP_REMIND_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=HELP_REMIND_ID))

    @staticmethod
    def __create_cancel_help_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(HelpButtonsMarkup.__HELP_CANCEL_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=HELP_CANCEL_ID))

    @staticmethod
    def __create_help_help_button() -> InlineKeyboardButton:
        return types.InlineKeyboardButton(HelpButtonsMarkup.__HELP_HELP_COMMAND_BUTTON,
                                          callback_data=help_id.new(id=HELP_HELP_ID))
