# buttons.py fayli
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import calendar
from utils.env import ADMIN




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
EXCEL = "📥 Excel file yuklash"

CHECK_SHIPMENTS_RU = "📦 Проверить отправления"
ID_REGISTRATION_RU = "🪪 ID / Регистрация"
SETTINGS_RU = "⚙️ Настройки"
EXCEL_RU = "📥 Загрузить Excel файл"




def mainMenu(lang, user_id):
    if lang == 'uz':
        buttons = [
            [KeyboardButton(text=CHECK_SHIPMENTS)],
            [KeyboardButton(text=ID_REGISTRATION)],
            [KeyboardButton(text=SETTINGS)]
        ]
        excel_button = KeyboardButton(text=EXCEL)
    else:
        buttons = [
            [KeyboardButton(text=CHECK_SHIPMENTS_RU)],
            [KeyboardButton(text=ID_REGISTRATION_RU)],
            [KeyboardButton(text=SETTINGS_RU)]
        ]
        excel_button = KeyboardButton(text=EXCEL_RU)

    if user_id == ADMIN:
        buttons.append([excel_button])

    markup = ReplyKeyboardMarkup(
        keyboard=buttons,
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


def branch(branches, lang):
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    for branch_item in branches:
        name = branch_item['name']

        button = KeyboardButton(name)
        markup.add(button)
    
    if lang == "uz":
        markup.add(BACK_UZ)
    else:
        markup.add(BACK_RU)
        
    return markup
    

CONFIRM_UZ = "👍 Tasdiqlayman"
CONFIRM_RU = "👍 Подтверждаю"


def confirm(lang): 
    if lang == "uz":
        markup =ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(CONFIRM_UZ)],
                [KeyboardButton(BACK_UZ)]
            ],
            resize_keyboard=True
        )
    else:
        markup =ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(CONFIRM_RU)],
                [KeyboardButton(BACK_RU)]
            ],
            resize_keyboard=True
        )
        
    return markup
       



def admin_confirm(user_id):
    inlines = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"confirm_{user_id}"),
            ],
            [
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject_{user_id}")
            ]
        ]
    )
    return inlines



def edit_cancelled():
    new_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="❌ Ariza rad etildi", callback_data="no_action")
    )
    
    return new_markup

def edit_accepted():
    new_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="✅ Ariza qabul qilindi", callback_data="accepted_status")
    )
    
    return new_markup


def shipments(lang, category):
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    for category_item in category:
        name = category_item['name']

        button = KeyboardButton(name)
        markup.add(button)
    
    if lang == "uz":
        markup.add(BACK_UZ)
    else:
        markup.add(BACK_RU)
        
    return markup
    