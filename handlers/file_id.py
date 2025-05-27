# from aiogram.types import Message
# from aiogram.dispatcher import FSMContext
# from utils.env import ADMIN
# from loader import dp




# @dp.message_handler(content_types=['photo'])
# async def file_id(message: Message, state: FSMContext):
#     if message.chat.type == "private" and message.from_user.id == ADMIN:
#         photo_id = message.photo[-1].file_id
#         await message.answer(photo_id)
