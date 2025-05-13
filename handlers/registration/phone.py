from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from state.state import Register
from services.services import getUser
from loader import dp, bot
from utils.env import PASSPORT_ID_IMAGE
import re

PHONE_REGEX = re.compile(r'^\+?998\d{9}$')


@dp.message_handler(content_types=['text', 'contact'], state=Register.phone)
async def phone(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']

    if message.contact:
        phone = message.contact.phone_number
    else:
        text = str(message.text).strip()
        
        if not PHONE_REGEX.match(text):
            await message.answer(
                texts.INVALID_PHONE[lang],
            )
            return
        phone = text
        
    await state.update_data({
        "phone": phone
    })
    
    await message.answer_photo(
        photo=PASSPORT_ID_IMAGE,
        caption=texts.PASSPORT_ID[lang]
    )
