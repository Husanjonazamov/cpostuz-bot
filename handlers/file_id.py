from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from utils.env import ADMIN
from loader import dp, bot
from services.services import getUser
from utils import texts




@dp.message_handler(content_types=['photo'])
async def file_id(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    user_id = message.from_user.id
    if user_id == ADMIN:
        await message.answer(
            photo_id
        )
    else:
        username = message.from_user.username
        
        user = getUser(user_id)
        lang = user['data'][0]['lang']
        phone = user['data'][0]['phone']
        
        caption = texts.caption_text(
            username=username,
            phone=phone
        )
        
        await bot.send_photo(
            chat_id=ADMIN,
            photo=photo_id,
            caption=caption
        )
        
        await message.answer(
            texts.SUCCESS_SCREEN[lang]
        )
