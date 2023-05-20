from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаём клавиатуру через ReplyKeyboardBuilder -------

# Создаём кнопки с ответами согласия и отказа
button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

# Инициализируем билдер с кнопками "Давай" и "Не хочу"
yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметрами width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаём клавиатуру с кнопками "Давай" и "Не хочу"
yes_no_kb = yes_no_kb_builder.as_markup(one_time_keyboard=True,
                                        resize_keyboard=True)

# ------- Создаём игровую клавиатуру без использования билдера -------

# Создаём кнопки игровой клавиатуры
button_1: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

# Создаём игровую клавиатуру с кнопками "Камень", "Ножницы" и "Бумага" как список списков
game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1], [button_2], [button_3]], resize_keyboard=True)
