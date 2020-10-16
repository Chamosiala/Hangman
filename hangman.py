board = []
turns = 0
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append(' ')

print(f"""---------
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
---------""")

while 1:
    while 1:
        coords = input("Enter the coordinates: ").split()
        x = coords[0]
        y = coords[1]
        if not x.isalnum() or not y.isalnum():
            print("You should enter numbers!")
        elif int(x) > 3 or int(x) < 1 or int(y) > 3 or int(y) < 1:
            print("Coordinates should be from 1 to 3!")
        elif len(coords) > 2:
            print("You should only enter 2 numbers!")
        elif board[abs(int(y) - 3)][int(x) - 1] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            if turns % 2:
                board[abs(int(y) - 3)][int(x) - 1] = 'O'
            else:
                board[abs(int(y) - 3)][int(x) - 1] = 'X'
            turns += 1
            break

    print(f"""---------
| {board[0][0]} {board[0][1]} {board[0][2]} |
| {board[1][0]} {board[1][1]} {board[1][2]} |
| {board[2][0]} {board[2][1]} {board[2][2]} |
---------""")

    if (['X', 'X', 'X'] in board or board[0][0] == board[1][1] == board[2][2] == 'X'
            or board[0][2] == board[1][1] == board[2][0] == 'X'
            or board[0][0] == board[1][0] == board[2][0] == 'X'
            or board[0][1] == board[1][1] == board[2][1] == 'X'
            or board[0][2] == board[1][2] == board[2][2] == 'X'):
        print("X wins")
        break
    elif (['O', 'O', 'O'] in board or board[0][0] == board[1][1] == board[2][2] == 'O'
          or board[0][2] == board[1][1] == board[2][0] == 'O'
          or board[0][0] == board[1][0] == board[2][0] == 'O'
          or board[0][1] == board[1][1] == board[2][1] == 'O'
          or board[0][2] == board[1][2] == board[2][2] == 'O'):
        print("O wins")
        break
    elif turns == 9:
        print("Draw")
        break
