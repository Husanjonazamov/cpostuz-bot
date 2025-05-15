from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser
from utils.env import ADMIN
from state.state import ExcelCreateState
from io import BytesIO



@dp.message_handler(lambda message: message.text.startswith((
    buttons.EXCEL,
    buttons.EXCEL_RU
)), state="*")
async def excel_(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']

    await message.answer(
        texts.EXCEL[lang],
        reply_markup=buttons.mainBack(lang)
    )
    await ExcelCreateState.excel.set()    