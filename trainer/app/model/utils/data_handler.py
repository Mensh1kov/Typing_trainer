import json


def load_data(path: str) -> dict:
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def save_data(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_users() -> dict:
    return load_data('trainer/data/users.json')


def load_user_by_name(name: str) -> dict:
    users = load_users()
    return users.get(name, create_new_user(name))


def create_new_user(name: str) -> dict:
    return {'name': name,
            'texts': 0,
            'speed': 0,
            'mistakes': 0}


def save_users(users: dict):
    save_data('trainer/data/users.json', users)


def save_user(user: dict):
    users = load_users()
    users[user.get('name')] = user
    save_users(users)
