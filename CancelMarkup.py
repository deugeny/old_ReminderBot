from typing import Never, Final

from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.filters import cancel_remind_id


class CancelMarkup(InlineKeyboardMarkup):
    __CANCEL_BUTTON_CAPTION: Final = "Отменить"

    def __init__(self, message_id: str | None, keyboard=None, row_width=3):
        super().__init__(keyboard, row_width)
        self.__create_cancel_markup(message_id)

    @staticmethod
    def __create_cancel_button(message_id: str | None) -> InlineKeyboardButton:
        return types.InlineKeyboardButton(CancelMarkup.__CANCEL_BUTTON_CAPTION,
                                          callback_data=cancel_remind_id.new(id=message_id))

    def __create_cancel_markup(self, message_id: str | None) -> Never:
        self.row(CancelMarkup.__create_cancel_button(str(message_id)))
