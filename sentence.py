import json
import random
from enum import Enum


class Levels(Enum):
    SIMPLE = 'simple'
    MEDIUM = 'medium'
    HARD = 'hard'
    LEGENDARY = 'legendary'


def get_sentence():
    with open('resources/texts/database.json', encoding='utf-8') as f:
        data = json.load(f)

    return random.choice(data)


def get_sentence_by_lvl(lvl: Levels):
    with open('resources/texts/levels.json', encoding='utf-8') as f:
        data = json.load(f)

    return random.choice(data.get(lvl.value))
