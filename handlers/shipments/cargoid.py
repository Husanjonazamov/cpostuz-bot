from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getCategory
from state.state import CargoSearch



CARGO_UZ = "🔍 CargoID bo'yicha qidirish" 
CARGO_RU = "🔍 Поиск по CargoID"


@dp.message_handler(lambda message: message.text in (
    CARGO_UZ,
    CARGO_RU
), state="*")
async def shipments(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']


    await message.answer(
        texts.CARGO_ID[lang],
        reply_markup=buttons.mainBack(lang)
    )    
    await CargoSearch.cargo_id.set()
    
    
