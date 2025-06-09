from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getBranch
from state.state import Register    
from utils.env import PASSPORT_FRONT_IMAGE




@dp.message_handler(content_types=['text'], state=Register.branch)
async def branch_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']

    branches = getBranch(lang)  
    branch_names = [b['name'].strip().casefold() for b in branches]  

    branch = message.text.strip().casefold() 

    if message.text in [buttons.BACK_BASE_RU, buttons.BACK_BASE_UZ]:
        await message.answer(
            texts.ADDRESS[lang],
            reply_markup=buttons.baseBack(lang)
        )
        await Register.address.set()
    
    elif branch not in branch_names:
        await message.answer(
            texts.INVALID_BRANCH[lang],
            reply_markup=buttons.branch(branches,lang)
        )
        await Register.branch.set()
    else:
        original_branch_name = next(b['name'] for b in branches if b['name'].strip().casefold() == branch)

        await state.update_data({
            "branch": original_branch_name
        })
        
        await message.answer_photo(
            photo=PASSPORT_FRONT_IMAGE,
            caption=texts.PASSPORT_FRONT[lang],
            reply_markup=buttons.baseBack(lang)
        )
        await Register.passport_front.set()
