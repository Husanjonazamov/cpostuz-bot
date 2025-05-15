from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register
from utils.env import PASSPORT_JSH_IMAGE

import re

PASSPORT_REGEX = re.compile(r'^[A-Z]{2}\d{7}$')

@dp.message_handler(content_types=['text'], state=Register.passport_id)
async def passport_id_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    
    lang = user['data'][0]['lang']
    
    passport_id = str(message.text.strip().upper())
    
    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        await message.answer(
        texts.REGISTER_PHONE[lang],
        reply_markup=buttons.register_phone(lang)
        )
        await Register.phone.set()
    else:
        if not PASSPORT_REGEX.match(passport_id):
            await message.answer(texts.INVALID_PASSPORT_ID[lang])
            return
        
        await state.update_data({
            "passport_id": passport_id
        })
        
        await message.answer_photo(
            photo=PASSPORT_JSH_IMAGE,
            caption=texts.PASSPORT_JSH[lang],
            reply_markup=buttons.baseBack(lang)
        )
        
        await Register.passport_jsh.set()