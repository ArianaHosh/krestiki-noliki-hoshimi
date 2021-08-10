def name():
    print(" Игра 'Крестики-нолики' ")
    print(" ")
    print(" Как играть?? ")
    print(" ")
    print(" Нужно ввести 2 координаты! ")
    print(" Сначала введите цифру строки, ")
    print(" а затем цифру столбика ")
    print(" ")
    print(" Например: '0 1' ")
    print(" ")


def playground():
    print(f"  0 1 2")
    for i in range(3):
        row = " ".join(field[i])
        print(f"{i} {row}")


def ask():
    while True:
        x, y = map(int, input(" Ваш ход: ").split())

        if x<0 or x>2 or y<0 or y>2:
            print(" Неверные координаты! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята!")
            continue

        return x, y


def win():
    win_comb = ( ((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
                 ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)),
                 ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0)) )
    for comb in win_comb:
        symbols = []
        for c in comb:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O!!")
            return True
    return False


name()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    playground()
    if count % 2 == 1:
        print(" Ходит крестик! ")
    else:
        print(" Ходит нолик! ")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья! ")
        break

