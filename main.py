import random
import json
import csv
import os

player = {
    'name': 'Авантюрист',
    'health': 100,
    'inventory': [],
}

quests = [
    {
        'title': 'Задание 1',
        'description': 'Вас отправили на поиски древнего артефакта. Вы стоите перед двумя путями, на восток и на север. Куда отправитесь?',
        'options': {
            '1': 'Идти на восток',
            '2': 'Идти на север',
        },
        'correct_option': '1',
    },

    {
 'title': 'Задание 2',
 'description': 'Вы пришли в старую руину. В комнате вы видите сундук. Открыть его?',
 'options': {
 '1': 'Открыть сундук',
 '2': 'Пройти мимо',
        },
 'correct_option': '1',
    },
    {
 'title': 'Задание 3',
 'description': 'Вы нашли древний артефакт. Какое решение примете?',
 'options': {
            '1': 'Взять артефакт с собой',
            '2': 'Оставить его на месте',
        },
        'correct_option': '1',
    },
    {
        'title': 'Задание 4',
        'description': 'Вы столкнулись с загадочным порталом. Вернуться обратно или пройти через него?',
        'options': {
            '1': 'Пройти через портал',
            '2': 'Вернуться назад',
        },
        'correct_option': '2',
    },
    {
        'title': 'Задание 5',
        'description': 'Вас атакует стая диких животных. Как вы защититесь?',
        'options': {
            '1': 'Сразиться с ними',
            '2': 'Попытаться убежать',
        },
        'correct_option': '1',
    },
    {
        'title': 'Задание 6',
        'description': 'Вы наткнулись на сокровища в заброшенной пещере. Взять сокровища с собой?',
        'options': {
            '1': 'Взять сокровища',
            '2': 'Оставить их на месте',
        },
        'correct_option': '1',
    },
    {
        'title': 'Задание 7',
        'description': 'Вы наткнулись на странный алтарь с загадочными символами. Выберите действие:',
        'options': {
            '1': 'Прочитать символы',
            '2': 'Пройти мимо',
        },
        'correct_option': '1',
    },
    {
        'title': 'Задание 8',
        'description': 'Вам предстоит переплыть реку с быстрым течением. Что вы предпримете?',
        'options': {
            '1': 'Попытаться переплыть самостоятельно',
            '2': 'Искать брод',
        },
        'correct_option': '2',
    },
    {
        'title': 'Задание 9',
        'description': 'Вы видите огромное дерево с ярко светящимися плодами. Попробуете их съесть?',
        'options': {
            '1': 'Попробовать плоды',
            '2': 'Пройти мимо',
        },
        'correct_option': '1',
    },
]



def start_game():
    print("Добро пожаловать в наше приключение!")
    player_name = input("Введите имя своего персонажа: ")
    player['name'] = player_name
    play_game()



def end_game():
    if player['health'] <= 0:
        print('Игра окончена. Ваш персонаж проиграл.')
    else:
        print('Поздравляем! Вы успешно завершили приключение. Ваш инвентарь:')
        for item in player['inventory']:
            print(f'- {item}')
    exit()



def play_game():
    while player['health'] > 0 and len(quests) > 0:
        current_quest = random.choice(quests)
        display_quest(current_quest)

        player_choice = input('Что вы решаете сделать? ')

        if process_choice(current_quest, player_choice):
            player['inventory'].append(current_quest['title'])

        quests.remove(current_quest)

    end_game()



def display_quest(quest):
    print(f'{quest["title"]}: {quest["description"]}')
    for option, description in quest['options'].items():
        print(f'[{option}] {description}')



def process_choice(quest, choice):
    if choice == quest['correct_option']:
        print('Правильное решение!')
        return True
    else:
        print('Вы сделали неправильный выбор.')
        return False


save_file = 'game_save.json'
csv_file = 'game_data.csv'


def start_game():
    print("Добро пожаловать в наше приключение!")
    player_name = input("Введите имя своего персонажа: ")
    player['name'] = player_name


    if check_save():
        load_game()
    else:
        play_game()

def check_save():
    try:
        with open(save_file, 'r') as file:
            save_data = json.load(file)
        return True
    except FileNotFoundError:
        return False


def save_game():
    with open(save_file, 'w') as file:
        json.dump(player, file)
    print("Игра сохранена.")


def load_game():
    with open(save_file, 'r') as file:
        save_data = json.load(file)
    player.update(save_data)
    print("Игра загружена.")
    play_game()


def delete_save():
    if check_save():
        confirm = input("Вы уверены, что хотите удалить сохранение? (yes/no): ")
        if confirm.lower() == "yes":
            os.remove(save_file)
            print("Сохранение удалено.")
    else:
        print("Сохранения не найдено.")


def end_game():
    if player['health'] <= 0:
        print('Игра окончена. Ваш персонаж проиграл.')
    else:
        print('Поздравляем! Вы успешно завершили приключение. Ваш инвентарь:')
        for item in player['inventory']:
            print(f'- {item}')

    save_game()
    update_game_data()
    exit()


def play_game():
    while player['health'] > 0 and len(quests) > 0:
        current_quest = random.choice(quests)
        display_quest(current_quest)

        player_choice = input('Что вы решаете сделать? ')

        if process_choice(current_quest, player_choice):
            player['inventory'].append(current_quest['title'])

        quests.remove(current_quest)

    end_game()


def display_quest(quest):
    print(f'{quest["title"]}: {quest["description"]}')
    for option, description in quest['options'].items():
        print(f'[{option}] {description}')


def process_choice(quest, choice):
    if choice == quest['correct_option']:
        print('Правильное решение!')
        return True
    else:
        print('Вы сделали неправильный выбор.')
        return False


def update_game_data():
    game_data = []
    if os.path.isfile(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                game_data.append(row)

    player_data = [player['name'], str(player['health']), ', '.join(player['inventory'])]
    game_data.append(player_data)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(game_data)
    print("Данные игры обновлены.")


start_game()