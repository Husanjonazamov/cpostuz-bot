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
    
    # Short branch
    all_text = getIdBranch(int(branch))
    text = all_text['data']['branch_name']
    if text.lower() == 'toshobl':
        short_branch = text
    elif text.lower() == "toshkent":
        short_branch = "CP"
    else:
        short_branch = text[:3]

    await state.update_data({"user_id": user_id})

    accepted = getLocation()

    avto_text = ""
    avia_text = ""

    for loc in accepted:
        cargo_type = loc.get('cargo_type')
        location = loc.get('location')

        if cargo_type == "avto":
            avto_text = location.format(
                f"<code>{short_branch}{register_id}</code>",
                f"<code>{short_branch}{register_id}</code>",
                f"<code>{short_branch}{register_id}</code>"
            )
        
        elif cargo_type == "avia":
            avia_text = location.format(
                f"<code>{short_branch}{register_id}</code>",
                f"<code>{short_branch}{register_id}</code>",
                f"<code>{short_branch}{register_id}</code>",
                f"<code>{short_branch}{register_id}</code>"
            )

    result_parts = []

    if avto_text:
        result_parts.append("🚗 <b>Avto Cargo</b>:\n\n" + avto_text)

    if avia_text:
        result_parts.append("✈️ <b>Avia Cargo</b>:\n\n" + avia_text)

    result_text = "\n\n".join(result_parts)

    # Yuborish
    await bot.send_message(
        chat_id=user_id,
        text=result_text,
        parse_mode="HTML"
    )

    await callback.message.edit_reply_markup(reply_markup=buttons.edit_accepted())
    await state.finish()

