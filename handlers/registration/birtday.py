from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register
from utils.env import PASSPORT_JSH_IMAGE




@dp.message_handler(content_types=['text'], state=Register.birth_date)
async def birth_date_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    birth_date = message.text
    
    
    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        await message.answer_photo(
            photo=PASSPORT_JSH_IMAGE,
            caption=texts.PASSPORT_JSH[lang],
            reply_markup=buttons.baseBack(lang)
        )
        
        await Register.passport_jsh.set()
    else:
        await state.update_data({
            "birth_date": birth_date
        })
            
        await message.answer(
            texts.ADDRESS[lang],
            reply_markup=buttons.baseBack(lang)
        )
        await Register.address.set()