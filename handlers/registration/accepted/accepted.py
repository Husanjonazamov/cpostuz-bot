from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from services.services import getUser, putUser, getBranchId, getIdBranch
from loader import dp, bot
from state.state import Register, AdminVerifyCode
from utils.env import ADMIN




@dp.callback_query_handler(lambda call: call.data.startswith("confirm_"), state="*")
async def accepted(callback: CallbackQuery, state: FSMContext):
    callback_data = callback.data
    user_id = callback_data.split("_")[1]
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    branch = user['data'][0]['branch']
    register_id = user['data'][0]['id']
    
    
    all_text = getIdBranch(int(branch))
    text = all_text['data']['branch_name']
    if text.lower() == 'toshobl':
        short_branch = text  
    else:
        short_branch = text[:3]  
    
        
    await state.update_data({"user_id": user_id})

    await bot.send_message(
        chat_id=user_id,
        text=texts.ACCEPTED[lang].format(short_branch, register_id)
    )
    await callback.message.edit_reply_markup(reply_markup=buttons.edit_accepted())
    await state.finish()