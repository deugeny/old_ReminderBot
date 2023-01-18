from telebot.asyncio_handler_backends import State, StatesGroup


class CurrentState(StatesGroup):
    wait_cancel_data = State()
    wait_remind_data = State()
    wait_help_data = State()
