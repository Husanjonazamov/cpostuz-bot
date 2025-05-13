# buttons.py fayli
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

LANGUAGES_UZ = "🇺🇿 O'zbek tili"
LANGUAGES_RU = "🇷🇺 Русский язык"



def language():
    lang = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=LANGUAGES_UZ)
            ],
            [
                KeyboardButton(text=LANGUAGES_RU)
            ],
        ],
        resize_keyboard=True
    )
    return lang
