game_board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
# Starts the game.
def play():
    while True:
        start=input(f'Play? y/n ')
        
        if start.lower() == 'y':
            print("Let's play")
            break
        elif start.lower() == 'n':
            print("Farewell. Bye!")
        else:
            print("Type y or n.")
# Takes P1 user input 
def O_field_row():
    while True:
        O_row=input('O Choose a row. 1-3 ')
        if O_row.isdigit():
            O_row=int(O_row)
            if 1 <= O_row <= 3:
                print(f'You chose row {O_row}.')  
                break
            else:
                print("Invalid input. You have to choose between 1-3.")
    return O_row

def O_field_column():
    while True:
        O_column=input('O Choose a column. 1-3 ')
        if O_column.isdigit():
            O_column=int(O_column)
            if 1 <= O_column <= 3:
                print(f'You chose column {O_column}.')
                break
            else:
               print("Invalid input. You have to choose between 1-3.") 
    return O_column
#Takes P2 user input 
def X_field_row():
    while True:
        X_row=input('X Choose a row. 1-3 ')
        if X_row.isdigit():
            X_row=int(X_row)
            if 1 <= X_row <= 3:
                print(f'You chose row {X_row}.')  
                break
            else:
                print("Invalid input. You have to choose between 1-3.")
    return X_row

def X_field_column():
    while True:
        X_column=input('X Choose a column. 1-3 ')
        if X_column.isdigit():
            X_column=int(X_column)
            if 1 <= X_column <= 3:
                print(f'You chose column {X_column}.')
                break
            else:
               print("Invalid input. You have to choose between 1-3.") 
    return X_column
# checks the fileld if its empty
# Overwrites gameboard field form P1 input
def place_o():
    
    while True:
        row_index_O = O_field_row() - 1
        column_index_O = O_field_column() - 1
        if game_board[row_index_O][column_index_O] == "_":
            game_board[row_index_O][column_index_O] = "O"
            break
        else:
            print("Field already taken. Choose another.")

   
    for row in game_board:
        print(" ".join(row))
    
    return game_board

# checks the fileld if its empty
# Overwrites gameboard field form P2 input
def place_x():

    while True:
        row_index_X = X_field_row() - 1
        column_index_X = X_field_column() - 1
        if game_board[row_index_X][column_index_X] == "_":
            game_board[row_index_X][column_index_X] = "X"
            break
        else:
            print("Field already taken. Choose another.")


    for row in game_board:
        print(" ".join(row))

    return game_board
# Checks the gameboard field if someone won
def o_win_check():
    for row in game_board:
        if row == ['O', 'O', 'O']:
            return True
        
    for col in range(3):
        if all(game_board[row][col] == 'O' for row in range(3)):
            return True
        if all(game_board[i][i] == 'O' for i in range(3)) or all(game_board[i][2 - i] == 'O' for i in range(3)):
            return True
    
def x_win_check():
    for row in game_board:
        if row == ['X', 'X', 'X']:
            return True

    for col in range(3):
        if all(game_board[row][col] == 'X' for row in range(3)):
            return True
    
        if all(game_board[i][i] == 'X' for i in range(3)) or all(game_board[i][2 - i] == 'X' for i in range(3)):
            return True

def draw():
    check_list=[]
    for row in game_board:
        for i in row:
            if i == "_":
                check_list.append(i)

        if check_list == []:
            print("Draw!")
            return True
            
def replay():
    if o_win_check or x_win_check == False:
        for row_index, row in enumerate(game_board):
            for column_index, value in enumerate(row):
                if value == "O" or 'X':
                    game_board[row_index][column_index] = "_"

        main()
    elif draw() == True:
        for row_index, row in enumerate(game_board):
            for column_index, value in enumerate(row):
                if value == "O" or 'X':
                    game_board[row_index][column_index] = "_"

        main()
    else:
        pass

def main():
    play()
    while True:
        place_o()
        if o_win_check() == True:
            print("O has won!")
            break
        place_x()
        if x_win_check() == True:
            print('X has won!')
            break
        draw()
    replay()

main()