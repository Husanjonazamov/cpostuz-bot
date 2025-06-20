from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser, SearchId, getIdBranch
from state.state import CargoSearch
from datetime import datetime




@dp.message_handler(content_types=['text'], state=CargoSearch.cargo_id)
async def shipments(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    cargo_id = message.text.strip()
    search_data = SearchId(cargo_id)

    if search_data:

        try:
            date = datetime.strptime(search_data["DATE"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")
        except:
            date = search_data["DATE"]

        branch = user['data'][0]['branch']
        all_text = getIdBranch(int(branch))
        text = all_text['data']['branch_name']
        print(text)
        if text.lower() == 'toshobl':
            short_branch = "Tosh"
        elif text.lower() == "toshkent shahar":
            short_branch = "JV"
        else:
            short_branch = text[:3]

        register_id = user["data"][0]['id']

        qty = search_data.get('Q-TY', '-')
        reys = search_data.get('KG', '-')
        treck_number = search_data.get('TREK_NUMBER', '-')

        

        await message.answer(
            text=texts.track_item(
                qty=qty,
                reys=reys,
                treck_number=treck_number,
                date=date
            ),
            reply_markup=buttons.mainBack(lang),
            parse_mode="HTML"
        )
    else:
        await message.answer(
            texts.SEARCH_NOT[lang],
            reply_markup=buttons.mainBack(lang)
        )
