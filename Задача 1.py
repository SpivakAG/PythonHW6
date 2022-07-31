# Создайте программу для игры в "Крестики-нолики
from random import randint

pole = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
count = randint(1, 3)

def polePrint(pole):
    for i in range(0, len(pole)):
        for i2 in range(0, len(pole[i])):
            print(pole[i][i2], end=' ')
        print()

def WinCheck(pole):
    if pole[0][0] == pole[0][1] == pole[0][2] != '_' or pole[0][0] == pole[1][1] == pole[2][2] != '_' or pole[0][0] == pole[1][0] == pole[2][0] != '_' or pole[0][0] == pole[1][0] == pole[2][0] != '_' or pole[0][2] == pole[1][2] == pole[2][2] != '_' or pole[0][0] == pole[1][1] == pole[2][2] != '_' or pole[0][2] == pole[1][1] == pole[2][0] != '_' or pole[2][0] == pole[2][1] == pole[2][2] != '_':
        return True
    else:
        return False

def opponent(pole):
    x = randint(0, 2)
    y = randint(0, 2)
    print(f'Противник ходит на {x}, {y}')
    while pole[x][y] != '_':
        x = randint(0, 2)
        y = randint(0, 2)
    pole[x][y] = 'O'
    print('Ход противника принят')

def player(pole):
    x = int(input('Введите номер строки: '))
    y = int(input('Введите номер столбца: '))
    x -= 1
    y -= 1
    print(f'Игрок ходит на {x}, {y}')
    while pole[x][y] != '_':
        x =int(input('Поле уже занято, заново введите номер строки: '))+1
        y =int(input('Введите номер столбца: '))+1
        print(f'Игрок ходит на {x}, {y}')
    pole[x][y] = 'X'
    print('Ход игрока принят')

print(f'count={count}')
print('Игра начинается')
if count%2==0:
    print('Первым ходит игрок')
else:
    print('Первым ходит бот')
polePrint(pole)

while WinCheck(pole)!=True:
    if count%2==0:
        player(pole)
        polePrint(pole)
        count+=1
        if WinCheck(pole)==True:
            print('Игра окончена! Победил игрок')
            break
    else:
        opponent(pole)
        polePrint(pole)
        count+=1
        if WinCheck(pole)==True:
            print('Игра окончена! Победил бот')