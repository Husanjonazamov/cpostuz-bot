from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import ExcelCreate, getUser
from utils.env import ADMIN
from io import BytesIO
from state.state import ExcelCreateState



@dp.message_handler(content_types=['document'], state=ExcelCreateState.excel)
async def excel_(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']

    if user_id == ADMIN:    
        document = message.document    
        if not document.file_name.endswith('.xlsx'):
            await message.answer(texts.NOT_FORMAT[lang])
            return
        
        buffer = BytesIO()
        await document.download(destination=buffer)
        buffer.seek(0)  
        
        result = ExcelCreate(buffer, document.file_name)

        if result:
            await message.reply("✅ Fayl saqlandi!")
        else:
            await message.reply("❌ Faylni saqlashda xatolik yuz berdi.")
