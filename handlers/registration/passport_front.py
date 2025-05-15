from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getBranch
from state.state import Register    
from utils.env import PASSPORT_BACK_IMAGE


@dp.message_handler(content_types=['photo', 'text'], state=Register.passport_front)
async def passport_front_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    print(user_id)
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        branch = getBranch(lang)
        
        await message.answer(
            texts.BRANCH[lang],
            reply_markup=buttons.branch(branch, lang)
        )
        await Register.branch.set()
    else:
        passport_front = message.photo[-1].file_id
        await state.update_data({
            "passport_front": passport_front
        })
        
        await message.answer_photo(
            photo=PASSPORT_BACK_IMAGE,
            caption=texts.PASSPORT_BACK[lang],
            reply_markup=buttons.baseBack(lang)
        )
    
        await Register.passport_back.set()
    