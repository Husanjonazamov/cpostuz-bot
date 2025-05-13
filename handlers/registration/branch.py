from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register    
from utils.env import PASSPORT_FRONT_IMAGE



@dp.message_handler(content_types=['text'], state=Register.branch)
async def branch_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    branch = message.text
    
    await state.update_data({
        "branch": branch
    })
    
    await message.answer_photo(
        photo=PASSPORT_FRONT_IMAGE,
        caption=texts.PASSPORT_FRONT[lang],
        reply_markup=buttons.mainBack(lang)
    )
   
    await Register.passport_front.set()