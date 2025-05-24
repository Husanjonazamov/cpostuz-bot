from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from .menu import menu
from utils.env import ADMIN

@dp.message_handler(content_types=['photo'])
async def back_(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    
    
    await bot.send_photo(
        chat_id=ADMIN,
        photo=photo_id
    )
