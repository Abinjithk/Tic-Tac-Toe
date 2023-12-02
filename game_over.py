class GameOver:
    def __init__(self):
        self.game_over = False

    def check(self, board, move):
        if move % 2 == 0:
            choice = "X"
        else:
            choice = "O"

        # Check rows, columns, and diagonals for a win
        if (board[0] == board[1] == board[2] == choice or
                board[3] == board[4] == board[5] == choice or
                board[6] == board[7] == board[8] == choice or
                board[0] == board[4] == board[8] == choice or
                board[2] == board[4] == board[6] == choice or
                board[2] == board[5] == board[8] == choice or
                board[1] == board[4] == board[7] == choice or
                board[0] == board[3] == board[6] == choice):

            return True

        else:

            return False
