from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from services.services import getUser





@dp.message_handler(lambda message: message.text in (
    buttons.CHECK_SHIPMENTS,
    buttons.CHECK_SHIPMENTS_RU
), state="*")
async def shipments(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    lang = user['data'][0]['lang']
    
    
