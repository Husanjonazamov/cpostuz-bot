from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp, bot



@dp.message_handler(lambda message: message.text == (
    buttons.LANGUAGES_UZ,
    buttons.LANGUAGES_RU
    ), state="*")
async def lang_handler(message: Message, state: FSMContext):
    pass




