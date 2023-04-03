from random import randint


def greetings():
    print('Добро пожаловать в игру Крестики нолики.')
    print('Игроки должны поочереди ввести координаты Y и Х')
    print('Пусть победит Сильнейший!')


field = [[' ' for d in range(3)] for i in range(3)]


def draw_field(step=0, II=False):
    if II and step % 2 != 0:
        pass
    else:
        print('    0   1   2')
        print('  -------------')
        for i, el in enumerate(field):
            print(f'{i} | {el[0]} | {el[1]} | {el[2]} |')
            print('  -------------')


def next_step(step, II):
    def input_step(II):
        while True:
            if II:
                x, y = randint(0,2), randint(0,2)
            else:
                turn = input('Введите координаты через пробел: ')
                try:
                    x, y = int(turn[0]), int(turn[2])
                except:
                    print('Неправильный ввод. Вводить нужно координаты от 0 до 2')
                    continue
                if not 0 <= x <= 2 or not 0 <= y <= 2:
                    print('Выход за координаты. Вводить нужно от 0 до 2')
                    continue
            if field[x][y] != ' ':
                if not II:
                    print('Клетка занята! Выберите другие координаты')
                continue
            else:
                return x, y
    if step % 2 == 0:
        print('Ходит Х')
        x, y = input_step(False)
        field[x][y] = 'X'
        return step + 1
    elif II:
        print('За O Ходит компьютер')
        x, y = input_step(II)
        field[x][y] = 'O'
        return step + 1
    else:
        print('Ходит О')
        x, y = input_step(II)
        field[x][y] = 'O'
        return step + 1

def check_win(step):
    win_comb = (((0,0), (0,1), (0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                 ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((2,0),(2,1),(2,2)),
                 ((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0)))

    for o, t, f in win_comb:
        if field[o[0]][o[1]] == field[t[0]][t[1]] == field[f[0]][f[1]] != ' ':
            print(f'Победил {field[o[0]][o[1]]}')
            draw_field()
            return False
    if step == 9:
        print('Ничья!')
        draw_field()
        return False
    return True


"""Сама игра"""
game = True
step = 0
greetings()
I = input('Хотите поиграть с компьютером? Введите Y:')
II = any([I == 'y', I == 'Y'])
while game:
    draw_field(step, II)
    step = next_step(step, II)
    game = check_win(step)
