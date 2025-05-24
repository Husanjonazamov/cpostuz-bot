from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import ScreenState
from utils.env import ADMIN

@dp.message_handler(content_types=['photo'], state=ScreenState.photo)
async def back_(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    
    await bot.send_photo(
        chat_id=ADMIN,
        photo=photo_id
    )
    
    await message.answer(
        texts.SUCCESS_SCREEN[lang]
    )
