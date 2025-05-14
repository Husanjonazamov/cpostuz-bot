from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser




@dp.callback_query_handler(lambda call: call.data.startswith("reject_"))
async def cencelled(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data
    user_id = callback_data.split("_")[1]
    
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    register_id = user['data'][0]['id']
    
    await bot.send_message(
        chat_id=user_id,
        text=texts.CANCELLED[lang].format(register_id)
    )
    await callback.message.answer(
        texts.ADMIN_CANCELLED.format(register_id)
    )
    
    await callback.message.edit_reply_markup(reply_markup=buttons.edit_cancelled())