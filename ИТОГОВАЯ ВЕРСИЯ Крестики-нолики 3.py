print("")
print('Добро пожаловать в игру "Крестики-нолики"!')
print("")

#game_cage = list(range(1, 10)) # Все клетки поля, пронумерованные
game_cage = list(range(1, 10))

# Игровое поле
def area_3x3():
    print('_________________________')
    print('|__', game_cage[0],'__|__', game_cage[1], '__|__', game_cage[2],'__|')
    print('|__', game_cage[3], '__|__', game_cage[4], '__|__', game_cage[5], '__|')
    print('|__', game_cage[6], '__|__', game_cage[7], '__|__', game_cage[8], '__|')

print("Первый ход совершает игрок х!")

# Присваиваем значение клеточке
def value(p_move, arg):
    if p_move > 9 or p_move < 1 or game_cage[p_move - 1] in ('x', 'o'):
        return False
    game_cage[p_move - 1] = arg
    return True


# Проверка на выигрышную комбинацию
def win_check():
    win = False
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 7))
    for i in win_combo:
        if game_cage[i[0]] == game_cage[i[1]] == game_cage[i[2]] and game_cage[i[1]] in ('x', 'o'):
            win = game_cage[i[0]]
    return win

# Основная функция
def game():
    gamer = 'x'
    step = 1
    while (step <= 9) and (win_check() == False):
        print("")
        p_move = int(input("Игрок " + gamer + " , ведите число, соответсвующее номеру клетки, куда хотите сделать ход: "))

        if value(p_move, gamer):

            if gamer == 'x':
                gamer = 'o'
            else:
                gamer = 'x'

        else:
            print('Клетка уже занята/Введено неверное значение! Повторите ввод.')

        area_3x3()
        step += 1

    if step > 9:
        print('Количество ходов закончилось! Игра завершилась с результатом "Ничья"!')
    else:
        win_check()

area_3x3()
game()