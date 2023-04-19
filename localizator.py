import json


def load_locale(locale: str) -> dict:
    with open(f'resources/locale/{locale}_locale.json', encoding='utf-8') as f:
        return json.load(f)
