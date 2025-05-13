# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import createUser, getUser



@dp.message_handler(commands=['start'])
async def start_handler(message: Message, state: FSMContext):
    
    user_id = message.from_user.id
    
    user = getUser(user_id)
    
    if user:
        await message.answer(texts.START)
    else:
        await message.answer(
            texts.START_LANG,
            reply_markup=buttons.language()
        )