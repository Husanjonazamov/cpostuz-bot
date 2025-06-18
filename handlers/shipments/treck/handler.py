from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, getCategory
from state.state import TreckSearch





@dp.message_handler(lambda message: message.text in (
    buttons.CARGO_UZ,
    buttons.CARGO_RU
), state="*")
async def shipments(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']


    await message.answer(
        texts.BAND_TRECK[lang],
        reply_markup=buttons.mainBack(lang)
    )    
    await TreckSearch.treck_id.set()
    
    
