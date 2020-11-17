from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from keyboards.menu import menu
from loader import dp
from states.states import Status
from config import chat_1, chat_2, chat_3, password


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await Status.Password.set()
    await message.answer(f'Привет, {message.from_user.full_name}! Введи пароль.')


@dp.message_handler(state=Status.Password)
async def enter_pass(message: types.Message):
    if message.text == password:
        await message.answer(f'Пароль верный!')
        await Status.next()
        await message.answer("Выберите категорию для связи", reply_markup=menu)
    else:
        await message.answer(f'Неверный пароль, повторите ввод')


@dp.message_handler(Text(equals=["Логисты", "Менеджеры", "Операторы"]), state=Status.Keyboard)
async def send_message(message: types.Message,  state: FSMContext):
    await message.answer(f"Вы выбрали {message.text}. "
                         f"Отправьте сообщение чтобы связаться с работником выбранной категории",)
    answer = message.text
    await state.update_data(answer1=answer)
    await Status.Question.set()


@dp.message_handler(state=Status.Question)
async def ask_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get("answer1")
    if answer == "Логисты":
        chat_id = chat_1
    elif answer == "Менеджеры":
        chat_id = chat_2
    elif answer == "Операторы":
        chat_id = chat_3
    else:
        await message.answer("Не понял")
    await Status.Keyboard.set()
    await message.forward(chat_id)
