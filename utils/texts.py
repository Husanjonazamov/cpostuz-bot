# texts.py fayli
START = {
    "uz": "Assalomu alaykum. 🌟 Xush kelibsiz!",
    "ru": "Привет. 🌟Добро пожаловать!"
}

START_LANG = \
"""
🔷 Tilni tanlang
"""

SETTINGS_HANDLER = {
    "uz": "Tilni tanlang!",
    "ru": "Выберите язык!"
}


NAME_UZ = \
"""
🪪 Ro'yxatdan o'tishingiz va CargoID olishingiz uchun siz quyidagi ketma-ketlikni to'ldirishingiz kerak bo'ladi:

 🔖 Ism-familyangizni kiriting: 
 Namuna: Azamov Husanboy 

 ❗️Eslatma: Hurmatli mijiz agar passport yoki ID kartadagi ism-familyanigizni kiritmasangiz sizning so'rovingiz bekor qilinishi mumkin!
"""

NAME_RU = \
"""
🪪 Чтобы зарегистрироваться и получить CargoID, вам необходимо выполнить следующую последовательность действий:

 🔖 Введите свое имя и фамилию: 
 Пример: Azamov Husanboy 

 ❗️Примечание: Уважаемый клиент, если вы не введете свои имя и фамилию из паспорта или ID-карты, ваш запрос может быть аннулирован!
"""


REGISTER_NAME = {
    "uz": NAME_UZ,
    "ru": NAME_RU
}


REGISTER_PHONE = {
    "uz": "📞 Telefon raqamingizni kiriting yoki quyidagi tugmani bosib yuboring.\n📱 Namuna: +998940014741",
    "ru": "📞 Введите свой номер телефона или нажмите на кнопку ниже.\n📱 Пример: +998940014741"
}


PASSPORT_ID_UZ = \
"""
🪪 Passport seriya raqamingizni kiriting:

 Namuna yuqoridagi rasmdagi: AA0000001 

 ❗️Eslatma: Hurmatli mijiz agar passport yoki ID kartadagi seria raqamingizni kiritmasangiz sizning so'rovingiz bekor qilinishi mumkin!
"""

PASSPORT_ID_RU = \
"""
🪪 Введите серийный номер вашего паспорта:

 Образец на картинке выше: AA0000001 

 ❗️Примечание: Уважаемый господин, если вы не введете серийный номер паспорта или удостоверения личности, ваш запрос может быть быть отменено!
"""

PASSPORT_ID = {
    "uz": PASSPORT_ID_UZ,
    "ru": PASSPORT_ID_RU
}

INVALID_PHONE = {
    "uz": "☎️ Iltimos, telefon raqamingizni to‘g‘ri kiriting:\n\nNamuna: +998901234567",
    "ru": "☎️ Пожалуйста, введите корректный номер телефона:\n\nПример: +998901234567"
}


INVALID_PASSPORT_ID = {
    "uz": "❌ Passport seriya raqami noto‘g‘ri!\n\n✅ Namuna: <b>AA1234567</b>",
    "ru": "❌ Серия и номер паспорта недействительны!\n\n✅ Пример: <b>AA1234567</b>",
}



PASSPORT_JSH_UZ = \
"""
🪪 Passport JShShIR(PINFL) raqamingizni kiriting:

 Namuna yuqoridagi rasmdagi: 30101800050014 

 ❗️Eslatma: Hurmatli mijiz agar passport yoki ID kartadagi JShShIR(Pinfl) raqamingizni kiritmasangiz sizning so'rovingiz bekor qilinishi mumkin!
"""


PASSPORT_JSH_RU = \
"""
🪪 Введите номер вашего паспорта JShSHIR(PINFL):

 Образец на картинке выше: 30101800050014 

 ❗️Примечание: Уважаемый клиент, если вы не введете свой номер JShShIR(PINFL) со своего паспорт или ID-карта, возможно, Ваш запрос будет отменен!
"""

PASSPORT_JSH = {
    "uz": PASSPORT_JSH_UZ,
    "ru": PASSPORT_JSH_RU
}


INVALID_JSHSHIR = {
    "uz": "❌ JShShIR noto‘g‘ri!\n\n✅ Namuna: <b>30101800050014</b>",
    "ru": "❌ Неправильный ИНН (JShShIR)!\n\n✅ Пример: <b>30101800050014</b>",
}


REQUEST_BIRTHDAY = {
    "uz": "🔢 Passportdagi tug'ilgan kun, oy, yilingiz:\n\nNamuna: 24.04.2004",
    "ru": "🔢 Дата рождения, указанная в паспорте:\n\nПример: 24.04.2004",
}


ADDRESS = {
    "uz": "🏡 To'liq manzilingizni kiriting:\n\nNamuna: Toshkent shahri, Yunusobod tumani 10-kvartal, 65/4/45",
    "ru": "🏡 Введите ваш полный адрес:\n\nПример: город Ташкент, Юнусабадский район, 10-й квартал, 65/4/45"
}


BRANCH = {
    "uz": "📍 O'zingizga qulay filialni tanlang:",
    "ru": "📍 Выберите удобный для вас филиал:"
}



PASSPORT_FRONT = {
    "uz": "🪪 Passportingizni old tarafini yuklang (JShShIR va Seria raqamini tasdiqlash uchun): Namuna yuqoridagi rasmda\n\n‼️Eslatma: Faqat O’zbekiston respublikasi biometrik passporti yoki ID Kartasi bo’lishi shart, aks holda sizning so’rovingiz qabul qilinmaydi!",
    "ru": "🪪 Загрузите переднюю сторону вашего паспорта (для подтверждения ПИНФЛ и серийного номера): Образец на изображении выше\n\n‼️Примечание: Принимаются только биометрический паспорт или ID-карта Республики Узбекистан, в противном случае ваш запрос не будет принят!"
}


PASSPORT_BACK = {
    "uz": "🪪 Passportingizni orqa tarafini yuklang (JShShIR va Seria raqamini tasdiqlash uchun): Namuna yuqoridagi rasmda\n\n‼️Eslatma: Faqat O’zbekiston respublikasi biometrik passporti yoki ID Kartasi bo’lishi shart, aks holda sizning so’rovingiz qabul qilinmaydi!",
    "ru": "🪪 Загрузите обратную сторону паспорта (для подтверждения ПИНФЛ и серийного номера): Пример на изображении выше\n\n‼️Примечание: Принимаются только биометрические паспорта или ID-карты Республики Узбекистан. В противном случае ваш запрос не будет принят!",
}



def summary(**kwargs):
    summary = ''
    
    if kwargs['lang'] == 'uz':
        summary += f"👤 Ism: {kwargs['name']}\n"
        summary += f"📞 Telefon: {kwargs['phone']}\n"
        summary += f"🪪 Passport: {kwargs['passport_id']}\n"
        summary += f"🔢 Pinfl: {kwargs['passport_jsh']}\n"
        summary += f"📅 Tug'ilgan kun: {kwargs['birth_date']}\n"
        summary += f"📍 Manzil: {kwargs['address']}\n"
        summary += f"🏢 Filial: {kwargs['branch']}\n"
    else:
        summary += f"👤 Имя: {kwargs['name']}\n"
        summary += f"📞 Телефон: {kwargs['phone']}\n"
        summary += f"🪪 Паспорт: {kwargs['passport_id']}\n"
        summary += f"🔢 ПИНФЛ: {kwargs['passport_jsh']}\n"
        summary += f"📅 Дата рождения: {kwargs['birth_date']}\n"
        summary += f"📍 Адрес: {kwargs['address']}\n"
        summary += f"🏢 Филиал: {kwargs['branch']}\n"

        
    return summary



CONFIRM = {
    "uz": "✅ Ma'lumotlaringiz to'g'riligini tasdiqlaysizmi?",
    "ru": "✅ Ma'lumotlaringiz to'g'riligini tasdiqlaysizmi?"
}


SEND_ADMIN = {
    "uz": "🥳 Sizning #{} raqamli so'rovingiz qabul qilindi!",
    "ru": "🥳 Ваш запрос с номером {} был принят!"
}


ADMIN_CONFIRM = \
"""
✅ Tasdiqlaysizmi? Arizani ko‘rib chiqqaningizdan so‘ng tasdiqlash yoki rad etishni tanlang.
"""

ENTER_CODE = {
    "uz": "🔐 Kodni kiriting:",
    "ru": "🔐 Введите код:"
}




CANCELLED = {
    "uz": "Hurmatli mijoz sizning #{} so'rovingiz rad etildi!\n\n📝 Sabab: Passport ma'lumotlari siz yozgan ma'lumotlarga to'g'ri kelmaganligi uchun bo'lishi mumkin!\nIltimos passport ma'lumotlaringiz bo'yicha ro'yxatdan o'ting.",
    "ru": "Уважаемый клиент, ваш запрос №{} был отклонён!\n\n📝 Причина: Возможно, данные паспорта не соответствуют введённой вами информации.\nПожалуйста, повторно зарегистрируйтесь, указав корректные паспортные данные."
}


ADMIN_CANCELLED  = \
"""
Siz #{} arizani bekor qildingiz
"""



SHIPMENTS = {
    "uz": "Kerakli bo'limni tanlang!",
    "ru": "Выберите нужный раздел!"
}


CARGO_ID = {
    "uz": "Cargo IDni kiriting!",
    "ru": "Введите Cargo ID!"
}


TRACK_ID = {
    "uz": "Trek IDni kiriting!",
    "ru": "Введите Trek ID!"
}


SEARCH_SUCCESFULL = {
    "uz": "✅ Sizning ushbu raqamli buyurtmangiz yetib keldi.",
    "ru": "✅ Ваш заказ с этим номером прибыл.",
}

SEARCH_NOT = {
    "uz": "❌ Kechirasiz, siz kiritgan raqamli buyurtma topilmadi. Iltimos, raqamni qayta tekshirib ko‘ring.",
    "ru": "❌ Извините, заказ с этим номером не найден. Пожалуйста, проверьте номер и попробуйте снова.",
}


BAND_TRECK = {
    "uz": "❌ Kechirasiz, bu bo‘lim hozircha yopiq.",
    "ru": "❌ Извините, этот раздел сейчас закрыт."
}

EXCEL = {
    "uz": "Iltimos, Excel faylni kiriting 📥",
    "ru": "Пожалуйста, загрузите Excel файл 📥"
}

OLD_REGISTER = {
    "uz": "❗️Siz allaqachon ro'yxatdan o'tgansiz. ID: #{}",
    "ru": "❗️Вы уже зарегистрированы. ID: #{}"
}


SEND_CODE = {
    "uz": "✅ Tasdiqlash kodi yuborildi.",
    "ru": "✅ Код подтверждения отправлен."
}




CARGO_AVIA = {
    "uz": """<b>№{order_id} so'rovingiz bo'yicha sizga</b>

✈️🆔 <b>Avia Cargo ID:</b> <code>{city_code}{cargo_id}</code>

✈️ <b>Avia sklad manzili:</b>
收货人: <code>{city_code}{cargo_id}</code>  
手机号码: <code>18335530701</code>  
<a href="{map_link}">北京市顺义区南法信旭辉空港中心C座1004 {city_code}{cargo_id}📌</a>  
(ushbu stiker yonidagi matnga bosish orqali manzilni ko‘chirib olishingiz mumkin)

<b>Avia post code:</b> <code>{post_code}</code>📌
""",

    "ru": """<b>По вашему запросу №{order_id} предоставлена информация</b>

✈️🆔 <b>Avia Cargo ID:</b> <code>{city_code}{cargo_id}</code>

✈️ <b>Адрес авиа склада:</b>  
Получатель: <code>{city_code}{cargo_id}</code>  
Телефон: <code>18335530701</code>  
<a href="{map_link}">北京市顺义区南法信旭辉空港中心C座1004 {city_code}{cargo_id}📌</a>  
(нажмите на текст рядом со стикером, чтобы скопировать адрес)

<b>Avia почтовый индекс:</b> <code>{post_code}</code>📌
"""
}




CARGO_AVTO = {
    "uz": """<b>№{order_id} so'rovingiz bo'yicha sizga</b>

🚗🆔 <b>Avto Cargo ID:</b> <code>{city_code}{cargo_id}</code>

🚗 <b>Avto sklad manzili:</b>  
收件人∶吴彦祖AT(<code>{city_code}{cargo_id}</code>)  
地址∶广州市白云区龙归街道南村攀龙六巷30号AТ(<code>{city_code}{cargo_id}</code>)  
电话: <code>18023847617</code>📌  
(ushbu stiker yonidagi matnga bosish orqali manzilni ko‘chirib olishingiz mumkin)

<b>Avto post code:</b> <code>{post_code}</code>📌
""",

    "ru": """<b>По вашему запросу №{order_id} предоставлена информация</b>

🚗🆔 <b>Avto Cargo ID:</b> <code>{city_code}{cargo_id}</code>

🚗 <b>Адрес авто склада:</b>  
Получатель: 吴彦祖AT(<code>{city_code}{cargo_id}</code>)  
Адрес: 广州市白云区龙归街道南村攀龙六巷30号AТ(<code>{city_code}{cargo_id}</code>)  
Телефон: <code>18023847617</code>📌  
(нажмите на текст рядом со стикером, чтобы скопировать адрес)

<b>Avto почтовый индекс:</b> <code>{post_code}</code>📌
"""
}



CHANNEL = {
    'uz': "❗️ Iltimos, kanalga obuna bo'ling:",
    'ru': "❗️ Пожалуйста, подпишитесь на канал:",
}


MESSAGES = \
    """
    Siz hali obuna bo'lmadingiz
    """

