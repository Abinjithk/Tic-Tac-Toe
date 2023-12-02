from game_over import GameOver
from board import Board

play = input("Do you want to play Tic-Tac-Toe (Enter Y or N) : ").upper()

if play == "Y":
    game_on = True
    move = 0
    board = Board()
    game_over = GameOver()
    while game_on:
        board.show_board()
        choice = int(input(f"player {move%2+1} enter the position of your move(1-9) : "))
        board.add(position=choice)
        if game_over.check(board=board.board_list,move=move):
            print(f"player {move%2+1} win the match")
            board.show_board()
            game_on = False
        elif move > 7:
            print("It's a draw")
            board.show_board()
            game_on = False

        move += 1


