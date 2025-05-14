from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, SearchId
from state.state import CargoSearch




@dp.message_handler(content_types=['text'], state=CargoSearch.cargo_id)
async def shipments(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    cargo_id = message.text
    print(cargo_id)
    
    search_data = SearchId(cargo_id)
    
    if search_data:
        await message.answer(
            texts.SEARCH_SUCCESFULL[lang],
            reply_markup=buttons.mainBack(lang)
        )
    else:
        await message.answer(
            texts.SEARCH_NOT[lang],
            reply_markup=buttons.mainBack(lang)
        )
    
    
    
