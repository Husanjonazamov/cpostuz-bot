from loader import bot
from utils.env import CHANNEL_ID

async def check_group_membership(user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False
