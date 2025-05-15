from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getBranch
from state.state import Register





@dp.message_handler(content_types=['text'], state=Register.address)
async def address_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    address = message.text
    
    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        await message.answer(
            texts.REQUEST_BIRTHDAY[lang],
            reply_markup=buttons.mainBack(lang)
        )
        
        await Register.birth_date.set()
    else:    
        await state.update_data({
            "address": address
        })
        
        branch = getBranch(lang)
        
        await message.answer(
            texts.BRANCH[lang],
            reply_markup=buttons.branch(branch, lang)
        )
        await Register.branch.set()

