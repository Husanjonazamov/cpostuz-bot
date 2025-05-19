from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from .handler import check_subscription
from utils.texts import MESSAGES
from services.services import getUser
from utils import texts, buttons


@dp.callback_query_handler(lambda c: c.data.startswith('check_sub'))
async def process_check_sub(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data.split(':')
    
    user_id = callback_query.data.split("_")[2]
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    from handlers.menu import menu  


    user_id = callback_query.from_user.id
    is_subscribed = await check_subscription(user_id)
    message = callback_query.message

    if is_subscribed:
        await callback_query.message.delete()
        await message.answer(
            texts.START[lang],
            reply_markup=buttons.mainMenu(lang, user_id)
        )   
        await state.finish()
    else:
        await bot.answer_callback_query(callback_query.id, text=MESSAGES)
