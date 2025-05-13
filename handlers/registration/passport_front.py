from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register    
from utils.env import PASSPORT_BACK_IMAGE



@dp.message_handler(content_types=['photo'], state=Register.passport_front)
async def passport_front_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    passport_front = message.photo[-1].file_id
    
    await state.update_data({
        "passport_front": passport_front
    })
    
    await message.answer_photo(
        photo=PASSPORT_BACK_IMAGE,
        caption=texts.PASSPORT_FRONT[lang],
        reply_markup=buttons.mainBack(lang)
    )
   
    await Register.passport_back.set()
    