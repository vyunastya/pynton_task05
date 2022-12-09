# 2 b) Подумайте как наделить бота ""интеллектом""
# Не делаю проверку ввода данных
import random


def turn_player(amount):
    candy = int(input(f'Игрок, сколько возьмёшь? '))
    amount -= candy
    print(f'Осталось {amount} конфет')
    return amount


total = 60
start = random.randint(0, 1)
print(f'Всего {total} конфет')
if start:
    print('Первый ходит человек')
    while total > 0:
        total = turn_player(total)
        win = 'человек'
        if total > 0:
            if total > 28:
                if total % 29 != 0:
                    bot = total % 29
                else:
                    bot = random.randint(1, 28)
            else:
                bot = total
            total -= bot
            print(f'Бот взял {bot}. Осталось {total} конфет')
            win = 'бот'
else:
    print('Первый ходит бот')
    while total > 0:
        if total > 28:
            if total % 29 != 0:
                bot = total % 29
            else:
                bot = random.randint(1, 28)
        elif total > 0:
            bot = total
        total -= bot
        print(f'Бот взял {bot}. осталось {total} конфет')
        win = 'бот'
        if total > 0:
            total = turn_player(total)
            win = 'человек'
print(f'Выиграл {win}')
