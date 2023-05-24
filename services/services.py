import random
from lexicon.lexicon_ru import LEXICON_RU


# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


# Функция, возвращающая ключ из словаря, по которому хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key


# Функция, определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'scissors': 'paper',
                             'paper': 'rock',
                             'rock': 'lizard',
                             'lizard': 'spock',
                             'spock': 'scissors',
                             'scissors_1': 'lizard',
                             'paper_1': 'spock',
                             'rock_1': 'scissors',
                             'lizard_1': 'paper',
                             'spock_1': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice or rules[user_choice + '_1'] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
