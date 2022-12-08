# 2b) Подумайте как наделить бота ""интеллектом""
# Боту позволено пропускать ход

import random


def turn_player(amount):
    candy = int(input(f'Игрок, сколько возьмёшь? '))
    amount -= candy
    return amount


total = 100
start = random.randint(0, 1)
print(f'Всего {total} конфет')
if start:
    print('Первый ходит человек')
    while total > 0:
        total = turn_player(total)
        win = 'человек'
        if total > 28:
            bot = total % 29
        elif total > 0:
            bot = total
        total -= bot
        print(f'Бот взял {bot}. осталось {total} конфет')
        win = 'бот'
else:
    print('Первый ходит бот')
    while total > 0:
        if total > 28:
            bot = total % 29
        elif total > 0:
            bot = total
        else:
            break
        total -= bot
        print(f'Бот взял {bot}. осталось {total} конфет')
        win = 'бот'
        if total != 0:
            total = turn_player(total)
            win = 'человек'
print(f'Выиграл {win}')
