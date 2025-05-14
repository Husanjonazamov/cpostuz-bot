from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from services.services import getUser, putUser
from loader import dp, bot









@dp.callback_query_handler(lambda call: call.data.startswith("confirm_"))
async def accepted(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data
    user_id = callback_data.split("_")[1]
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    register_id = user['data'][0]['id']


    await bot.send_message(
        chat_id=user_id,
        text=texts.ACCEPTED[lang].format(register_id)
    )

#  user = {
#         "name": name,
#         "phone": phone,
#         "passport_id": passport_id,
#         "passport_jsh": passport_jsh,
#         "birth_date": birth_date,
#         "address": address,
#         "branch": branch,
#     }
    
#     putUser(user_id, user)
        
    