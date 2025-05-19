from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from services.services import getUser, putUser, getBranchId, getIdBranch, getLocation
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
    elif text.lower() == "toshkent":
        short_branch = text[:4]  
    else:
        short_branch = text[:3]  
    
        
    await state.update_data({"user_id": user_id})
    
    accepted = getLocation()

    for loc in accepted:
        if loc['cargo_type'] == 'avia':
            cargo_avia_maps_link = loc['map_link']
            cargo_avia_post_code = loc['post_code']
        elif loc['cargo_type'] == 'avto':
            cargo_avto_maps_link = loc['map_link']
            cargo_avto_post_code = loc['post_code']

    if len(accepted) == 1:
        for loc in accepted:
            maps_link = loc['map_link']
            cargo_type = loc['cargo_type']
            post_code = loc['post_code']
            
    
        if cargo_type == "avia":
            await bot.send_message(
                    chat_id=user_id,
                    text=texts.CARGO_AVIA[lang].format(
                        order_id=register_id,
                        city_code=short_branch,
                        cargo_id=register_id,
                        map_link=maps_link,
                        post_code=post_code
                    ),
                    parse_mode="HTML"
                )
        elif cargo_type == "avto":
            await bot.send_message(
                    chat_id=user_id,
                    text=texts.CARGO_AVTO[lang].format(
                        order_id=register_id,
                        city_code=short_branch,
                        cargo_id=register_id,
                        map_link=maps_link,
                        post_code=post_code
                    ),
                    parse_mode="HTML"
                )
    else:
        await bot.send_message(
                chat_id=user_id,
                text=texts.CARGO_INFO[lang].format(
                    order_id=register_id,
                    city_code=short_branch,
                    cargo_id=register_id,
                    cargo_avto_maps_link=cargo_avto_maps_link,
                    cargo_avto_post_code=cargo_avto_post_code,
                    cargo_avia_maps_link=cargo_avia_maps_link,
                    cargo_avia_post_code=cargo_avia_post_code,
                ),
                parse_mode="HTML"
            )
        
    await callback.message.edit_reply_markup(reply_markup=buttons.edit_accepted())
    await state.finish()
    
    
