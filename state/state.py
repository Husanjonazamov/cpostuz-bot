# state.py fayli
from aiogram.dispatcher.filters.state import State, StatesGroup


class lang(StatesGroup):
    lang = State()
    
    
class Putlang(StatesGroup):
    lang = State()
    
    
class Register(StatesGroup):
    name = State()
    phone = State()
    passport_id = State()
    passport_jsh = State()
    birth_date = State()
    address = State()
    branch = State()
    passport_front = State()
    passport_back = State()
    confirm = State()
    
    
class CargoSearch(StatesGroup):
    cargo_id = State()
    
    
class TreckSearch(StatesGroup):
    treck_id = State()
    
    
class ExcelCreateState(StatesGroup):
    excel = State()
    
    
class AdminVerifyCode(StatesGroup):
    user_id = State()
    code = State()