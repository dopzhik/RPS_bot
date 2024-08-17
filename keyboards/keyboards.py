from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import lexicon_ru

button_yes = KeyboardButton(text=lexicon_ru['yes_button'])
button_no = KeyboardButton(text=lexicon_ru['no_button'])
button_stat = KeyboardButton(text=lexicon_ru['stat'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no, button_stat, width=2)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

button_1 = KeyboardButton(text=lexicon_ru['rock'])
button_2 = KeyboardButton(text=lexicon_ru['scissors'])
button_3 = KeyboardButton(text=lexicon_ru['paper'])

game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)
