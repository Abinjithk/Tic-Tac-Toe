class Board:
    def __init__(self):
        self.board_list = [" "," "," "," "," "," "," "," "," "]
        self.move = 1

    def add(self,position):

        if self.move % 2 != 0 and self.board_list[position-1]=="":
            self.board_list[position-1] = "X"
            self.move += 1
        elif self.board_list[position-1] == "X" or self.board_list[position-1] == "O":
            choice = int(input("position already filled re enter the position again (1-9) : "))
            self.add(choice)
        else:
            self.board_list[position-1] = "O"
            self.move += 1

    def show_board(self):
        print("_____________")
        print(f"| {self.board_list[0]} | {self.board_list[1]} | {self.board_list[2]} |")
        print("-------------")
        print(f"| {self.board_list[3]} | {self.board_list[4]} | {self.board_list[5]} |")
        print("_____________")
        print(f"| {self.board_list[6]} | {self.board_list[7]} | {self.board_list[8]} |")
        print("-------------")
