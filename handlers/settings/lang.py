from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp, bot
from ..menu import menu
from services.services import putUser
from state.state import Putlang



@dp.message_handler(lambda message: message.text in (
    buttons.LANGUAGES_UZ,
    buttons.LANGUAGES_RU
), state=Putlang.lang)

async def lang_handler(message: Message, state: FSMContext):
    lang = message.text
    user_id = message.from_user.id

    lang_codes = {
        buttons.LANGUAGES_UZ: 'uz',
        buttons.LANGUAGES_RU: 'ru',
    }
    
    
    if not lang in lang_codes:
        """
        Agar user xato til kiritsa
        """
        await message.delete()
        return

    lang = lang_codes[lang]

    await state.set_data({
        'lang': lang
    })

    putUser(user_id, lang)
    await menu(message, state)




