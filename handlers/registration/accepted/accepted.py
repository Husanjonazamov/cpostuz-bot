from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from services.services import getUser, putUser, getBranchId
from loader import dp, bot
from state.state import Register



@dp.callback_query_handler(lambda call: call.data.startswith("confirm_"), state="*")
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
    
    await callback.message.edit_reply_markup(reply_markup=buttons.edit_accepted())