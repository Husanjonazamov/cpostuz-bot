from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp, bot
from state.state import Register
from services.services import getUser 



@dp.message_handler(content_types=['text'], state=Register.name)
async def name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    name = message.text
    await state.update_data({
        'name': name
    })  
    
    await message.answer(
        texts.REGISTER_PHONE[lang],
        reply_markup=buttons.register_phone(lang)
    )
    await Register.phone.set()