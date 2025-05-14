from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from .menu import menu


@dp.message_handler(lambda message: message.text.startswith((buttons.BACK_UZ, buttons.BACK_RU)), state="*")
async def back_(message: Message, state: FSMContext):
    await menu(message, state)
