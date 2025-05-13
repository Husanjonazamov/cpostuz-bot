from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp, bot
from services.services import  getUser
from state.state import Putlang




@dp.message_handler(lambda message: message.text in (
    buttons.SETTINGS,
    buttons.SETTINGS_RU
), state="*")
async def settings_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    
    lang = user['data'][0]['lang']
    
    await message.answer(
        texts.SETTINGS_HANDLER[lang],
        reply_markup=buttons.language()
    )
    await Putlang.lang.set()