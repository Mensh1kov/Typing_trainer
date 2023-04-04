import json
import random


def get_sentence():
    # Загружаем данные из файла
    with open('database.json', encoding='utf-8') as f:
        data = json.load(f)

    # Получаем список предложений
    sentences = data['sentences']

    # Выбираем случайное предложение
    random_sentence = random.choice(sentences)

    return random_sentence['text']
