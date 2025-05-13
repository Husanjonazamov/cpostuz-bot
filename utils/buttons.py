# buttons.py fayli
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

LANGUAGES_UZ = "🇺🇿 O'zbek tili"
LANGUAGES_RU = "🇷🇺 Русский язык"

BACK_UZ = "🔙 Ortga"
BACK_RU = "🔙 Назад"



def mainBack(lang):
    if lang == "uz":
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=BACK_UZ)]
            ],
            resize_keyboard=True
        )
    else:
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=BACK_RU)]
            ],
            resize_keyboard=True
        )

    return markup


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


CHECK_SHIPMENTS = "📦 Jo'natmalarni tekshirish"
ID_REGISTRATION = "🪪 ID / Ro‘yxatdan o‘tish"
SETTINGS = "⚙️ Sozlamalar"

CHECK_SHIPMENTS_RU = "📦 Проверить отправления"
ID_REGISTRATION_RU = "🪪 ID / Регистрация"
SETTINGS_RU = "⚙️ Настройки"


def mainMenu(lang):
    if lang == 'uz':
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=CHECK_SHIPMENTS)],
                [KeyboardButton(text=ID_REGISTRATION)],
                [KeyboardButton(text=SETTINGS)]
            ],
            resize_keyboard=True
        )
    else:  
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text=CHECK_SHIPMENTS_RU)],
                [KeyboardButton(text=ID_REGISTRATION_RU)],
                [KeyboardButton(text=SETTINGS_RU)]
            ],
            resize_keyboard=True
        )
    return markup



def register_phone(lang):
    if lang == "uz":
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📤 Telefon raqamni yuborish", request_contact=True)],
                [KeyboardButton(text=BACK_UZ)]
            ],
            resize_keyboard=True
        )
    else:
        markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📤 Отправить номер телефона", request_contact=True)],
                [KeyboardButton(text=BACK_RU)]
            ],
            resize_keyboard=True
        )
        
    return markup