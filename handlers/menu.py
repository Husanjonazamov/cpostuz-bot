from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from handlers.channel.handler import check_subscription




async def menu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    is_subscribed = await check_subscription(user_id)
    if is_subscribed:
        await message.answer(
            texts.START[lang],
            reply_markup=buttons.mainMenu(lang, user_id)
        )   
        await state.finish()
    else:
        await message.answer(
            texts.CHANNEL[lang],
            reply_markup=buttons.channel_check(user_id)
        )