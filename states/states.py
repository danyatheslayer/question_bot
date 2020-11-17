from aiogram.dispatcher.filters.state import StatesGroup, State


class Status(StatesGroup):
    Password = State()
    Keyboard = State()
    Question = State()
