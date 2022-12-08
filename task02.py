# 2 Создайте программу для игры с конфетами человек против человека. Не делаю проверку ввода данных
# Не проверяю данные на вход, пусть данные вводятся корректно
import random

total = 150 #уменьшила кол-во конфет
start = random.randint(0, 1)
print(f'Всего {total} конфет. Первый ходит {start + 1} игрок')
while total > 0:
    player = int(input(f'{start + 1} игрок. Сколько возьмёшь? '))
    total -= player
    print(f'Осталось {total} конфет')
    start = abs(start - 1)
if start:
    win = 1
else:
    win = 2
print(f'Выиграл {win} игрок')