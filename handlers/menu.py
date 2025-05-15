from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser





async def menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    await message.answer(
        texts.START[lang],
        reply_markup=buttons.mainMenu(lang, user_id)
    )   
    await state.finish()