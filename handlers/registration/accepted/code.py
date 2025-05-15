from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from services.services import getUser, putUser, getBranchId
from loader import dp, bot
from state.state import Register, AdminVerifyCode
from utils.env import ADMIN




@dp.message_handler(content_types=['text'], state=AdminVerifyCode.code)
async def accepted(message: Message, state: FSMContext):
    user = getUser(ADMIN)
    lang = user['data'][0]['lang']
    
    data = await state.get_data()
    user_id = data.get('user_id')
    
    code = message.text
    await bot.send_message(
        chat_id=user_id,
        text=texts.ACCEPTED[lang].format(code)
    )
    
    await message.answer(
        texts.SEND_CODE[lang]
    )
    user = {
        "cargo_code": code
    }
    
    putUser(user_id, user)
    
    await state.finish()
    