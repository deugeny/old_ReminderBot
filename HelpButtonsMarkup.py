from typing import Final, Iterable, Never, Callable

from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks.filters import help_id, HELP_REMIND_ID, HELP_CANCEL_ID, HELP_HELP_ID

HELP_MARKUP_COMMANDS: Iterable[str] = ("/remind", "/help", "/cancel", "/start", "/show")


class HelpButtonsMarkup(InlineKeyboardMarkup):
    __HELP_CANCEL_COMMAND_BUTTON: Final = 'help для cancel'
    __HELP_HELP_COMMAND_BUTTON: Final = 'help для help'
    __HELP_REMIND_COMMAND_BUTTON: Final = 'help для remind'

    def __init__(self, commands: Iterable[str] = HELP_MARKUP_COMMANDS, keyboard=None, row_width=3):
        super().__init__(keyboard, row_width)
        self.__create_help_buttons(commands)

    def __create_help_buttons(self, commands: Iterable[str]) -> Never:
        self.row(self.__get_buttons(commands))

    @staticmethod
    def __get_buttons(commands:Iterable[str]) -> Iterable[Callable[[], InlineKeyboardButton]]:
        for command in commands:
            if command == "/help":
                yield HelpButtonsMarkup.__create_help_help_button(),
            if command == "/cancel":
                yield HelpButtonsMarkup.__create_cancel_help_button(),
            if command == "/remind":
                yield HelpButtonsMarkup.__create_remind_help_button()

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
