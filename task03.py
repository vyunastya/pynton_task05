# 3 Создайте программу для игры в ""Крестики-нолики"".
# Человек с человеком. не проверяю корректность данных на входе

import random


def print_field(field):
    print(f'{field[0]} | {field[1]} | {field[2]}')
    print('_________')
    print(f'{field[3]} | {field[4]} | {field[5]}')
    print('_________')
    print(f'{field[6]} | {field[7]} | {field[8]}')
    print()


def func_win(field):
    win_pos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_pos:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return True
    return False


field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
start = random.randint(0, 1)
print(f'Первый ходит {start + 1} игрок')
list_char = ['O', 'X']
count = 0
while True:
    count += 1
    print_field(field)
    player = int(input(f'{start + 1} игрок. Твой ход {list_char[abs(start - 1)]}: '))
    field[player - 1] = list_char[abs(start - 1)]
    if func_win(field):
        print_field(field)
        print(f'Выиграл {start + 1} игрок')
        break
    start = abs(start - 1)
    if count == 9:
        print_field(field)
        print('Ничья')
        break