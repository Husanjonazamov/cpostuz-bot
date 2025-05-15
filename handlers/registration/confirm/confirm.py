from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from services.services import getUser, putUser, getBranchId
from utils import texts, buttons
from utils.env import ADMIN
from aiogram.types import InputMediaPhoto
from state.state import Register




@dp.message_handler(lambda message: message.text in (
    buttons.CONFIRM_UZ,
    buttons.CONFIRM_RU
), state=Register.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    users = getUser(user_id)
    lang = users['data'][0]['lang']
    register_id = users['data'][0]['id']
    
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    passport_id = data.get('passport_id') 
    passport_jsh = data.get('passport_jsh')
    birth_date = data.get('birth_date')
    address = data.get('address')
    branch = data.get('branch')
    passport_front = data.get('passport_front')
    passport_back = data.get("passport_back")
    
    caption = texts.summary(
        lang=lang,
        name=name,
        phone=phone,
        passport_id=passport_id,
        passport_jsh=passport_jsh,
        birth_date=birth_date,
        address=address,
        branch=branch,
        passport_front=passport_front,
        passport_back=passport_back
    )

    media_group = [
        InputMediaPhoto(passport_front, caption=caption),  
        InputMediaPhoto(passport_back)  
    ]
    
    await bot.send_media_group(
        chat_id=ADMIN,
        media=media_group
    )
    await bot.send_message(
        chat_id=ADMIN,
        text=texts.ADMIN_CONFIRM,
        reply_markup=buttons.admin_confirm(user_id)
    )
    
    
    await message.answer(
        texts.SEND_ADMIN[lang].format(register_id),
        reply_markup=buttons.mainMenu(lang, user_id)
    )
    
    branch_data = getBranchId(branch)
    branch_id = branch_data['data']['branch_id']
    print(branch_id)

    user = {
        "name": name,
        "phone": phone,
        "passport_id": passport_id,
        "passport_jsh": passport_jsh,
        "birth_date": birth_date,
        "address": address,
        "branch": branch_id,
        "passport_front": passport_front,
        "passport_back": passport_back
    }

    putUser(user_id, user)
    
    await state.finish()

    
    
    
