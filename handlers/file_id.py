from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils.env import ADMIN
from loader import dp




@dp.message_handler(content_types=['photo'])
async def file_id(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    if message.from_user.id == ADMIN:
        await message.answer(photo_id)





