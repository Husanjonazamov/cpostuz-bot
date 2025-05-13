# state.py fayli
from aiogram.dispatcher.filters.state import State, StatesGroup


class lang(StatesGroup):
    lang = State()
    
    
class Putlang(StatesGroup):
    lang = State()