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


def load_sentence():
    with open('resources/text/database.json', encoding='utf-8') as f:
        data = json.load(f)
    return random.choice(data)


def load_sentence_by_lvl(lvl: Level):
    with open('resources/text/levels.json', encoding='utf-8') as f:
        data = json.load(f)
    return random.choice(data.get(lvl.value))


def load_locale(locale: Locale) -> dict:
    with open(f'resources/locale/{locale.value}_locale.json', encoding='utf-8') as f:
        return json.load(f)
