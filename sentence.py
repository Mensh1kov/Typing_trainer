import json
import random


def get_sentence():
    with open('database.json', encoding='utf-8') as f:
        data = json.load(f)

    return random.choice(data)
