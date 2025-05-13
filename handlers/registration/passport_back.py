from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMediaPhoto


from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from state.state import Register



@dp.message_handler(content_types=['photo'], state=Register.passport_back)
async def passport_back_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    
    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    passport_id = data.get('passport_id') 
    passport_jsh = data.get('passport_jsh')
    birth_date = data.get('birth_date')
    address = data.get('address')
    branch = data.get('branch')
    passport_front = data.get('passport_front')
    passport_back = message.photo[-1].file_id
    
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
        chat_id=user_id,
        media=media_group
    )
    await message.answer(
        texts.CONFIRM[lang],
        reply_markup=buttons.confirm(lang)
    )
    
    