import json
import random
from enum import Enum


class Level(Enum):
    SIMPLE = 'simple'
    MEDIUM = 'medium'
    HARD = 'hard'
    LEGENDARY = 'legendary'


class Locale(Enum):
    RU = 'ru'
    EN = 'en'


def load_data(path: str) -> dict:
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def load_sentence():
    data = load_data('trainer/resources/texts/database.json')
    return random.choice(data)


def load_sentence_by_lvl(lvl: Level, locale: Locale) -> str:
    print(locale)
    data = load_data(f'trainer/resources/texts/{locale.value}_levels.json')
    return random.choice(data.get(lvl.value))


def load_locale(locale: Locale) -> dict:
    return load_data(f'trainer/resources/locale/{locale.value}_locale.json')


def load_user(user: str):
    data = load_data('trainer/resources/users.json')
    return data.get(user)
