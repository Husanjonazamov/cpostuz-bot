from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register
from datetime import datetime
import re
from utils.env import PASSPORT_ID_IMAGE


JSHSHIR_REGEX = re.compile(r'^\d{14}$')


@dp.message_handler(content_types=['text'], state=Register.passport_jsh)
async def passport_jsh_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    passport_jsh = str(message.text.strip())


    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        await message.answer_photo(
            photo=PASSPORT_ID_IMAGE,
            caption=texts.PASSPORT_ID[lang],
            reply_markup=buttons.baseBack(lang)
        )
        
        await Register.passport_id.set()
    else:
        if not JSHSHIR_REGEX.fullmatch(passport_jsh):
            await message.answer(texts.INVALID_JSHSHIR[lang])
            return
        
        await state.update_data({
            'passport_jsh': passport_jsh
        })
        
        
        await message.answer(
            texts.REQUEST_BIRTHDAY[lang],
            reply_markup=buttons.baseBack(lang)
        )
        
        await Register.birth_date.set()
        
            
        