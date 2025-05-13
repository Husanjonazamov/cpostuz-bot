from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register    



@dp.message_handler()
async def passport_front_handler(message: Message, state: FSMContext):
    pass