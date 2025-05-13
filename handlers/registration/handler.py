from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser



@dp.message_handler(lambda message: message.text in  (
    buttons.ID_REGISTRATION,
    buttons.ID_REGISTRATION_RU
), state='*')
async def registration_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    
    lang = user['data'][0]['lang']
    
    await message.answer(
        texts.REGISTER_NAME[lang]
    )