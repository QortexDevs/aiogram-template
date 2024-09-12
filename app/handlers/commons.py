from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.base import BaseStorage
from aiogram.types import (
    Message,
)
from keyboards.start import START_KEYBOARD

router = Router(name=__name__)


class StartForm(StatesGroup):
    name = State()
    age = State()


@router.message(CommandStart())
async def start(message: Message, state: BaseStorage) -> None:
    start_message = "Привет!\n" "Это бот\n" "Напиши свое ФИО"
    await message.answer(start_message)
    await state.set_state(StartForm.name)


@router.message(F.text, StartForm.name)
async def get_name(message: Message, state: BaseStorage) -> None:
    await state.update_data(name=message.text)
    message_ = f"{message.text}\n" "Теперь напиши свой возраст"
    await message.answer(message_, reply_markup=START_KEYBOARD)
    await state.set_state(StartForm.age)


@router.message(F.text, StartForm.age)
async def get_age(message: Message, state: BaseStorage) -> None:
    await state.update_data(age=message.text)
    await message.answer(f"Возраст: {message.text}")
    await message.answer("Спасибо за введенную информацию!")
    data = await state.get_data()
    msg_text = (
        f'Вас зовут <b>{data.get("name")}</b> и вам <b>{data.get("age")}</b> лет. '
        f'Спасибо за то, что ответили на мои вопросы.'
    )
    await message.answer(msg_text, parse_mode="HTML")
