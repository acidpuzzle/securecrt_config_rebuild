"""
Скрипт проходит по вложенным каталогам и меняет логин и пароль в конфигурациях securecrt
Конфиги обычно лежат тут: %USERPROFILE%\AppData\Roaming\VanDyke\Config\
"""

import re
import os


def config_search() -> list:
    configs_list = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.ini') and file != '__FolderData__.ini':
                path = os.path.join(root, file)  # формирование адреса
                configs_list.append(path)  # добавление адреса в список
    return configs_list


def replace_in_file(config_file, username_str: str = None, password_str: str = None) -> None:
    try:
        with open(config_file, encoding='UTF8') as old_config:
            text = old_config.read()

        text = re.sub(r'S:\"Username\"\S+', 'S:\"Username\"={}'.format(username_str), text)
        text = re.sub(r'S:\"Password V2\"\S+', 'S:\"Password V2\"={}'.format(password_str), text)
        text = re.sub(r'S:\"Color Scheme\"\S+', 'S:\"Color Scheme\"=Birds of Paradise', text)
        text = re.sub(r'S:\"Keyword Set\"\S+', 'S:\"Keyword Set\"=<None>', text)

        with open(config_file, "w", encoding='UTF8') as new_config:
            new_config.write(text)
    except OSError as error:
        print(error)


if __name__ == "__main__":
    username = ''  # тут прописать логин.
    password = ''  # тут прописать ХЭШ пароля, можно взять из уже сохраненного конфига с правильным паролем.

    for config in config_search():
        replace_in_file(config, username_str=username, password_str=password)
