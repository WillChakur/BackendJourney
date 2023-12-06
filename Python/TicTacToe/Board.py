import numpy as np

class Board:
    def __init__(self):
        self.board_spaces = np.full((3,3), "-")
        
    def is_empty(self, row, column):
        if self.board_spaces[row][column] == 0:
            return True
        else:
            return False
        
    def set_marker(self, row, column, marker):
        self.board_spaces[row][column] = marker
        
    def show_board(self):
        print("Tic-Tac-Toe Board")
        print("")
        print(self.board_spaces)
    
    def verify_line(self, line, marker):
        for i in range(3):
            if self.board_spaces[line][i] == marker:
                continue
            else: return False
        
        return True
           
    def verify_column(self, column, marker):
        for i in range(3):
            if self.board_spaces[i][column] == marker:
                continue
            else: return False
        
        return True
    
    def win_game(self, marker):
        for i in range(3):
            if self.verify_line(i, marker) == True:
                return True
            if self.verify_column(i, marker) == True:
                return True
            
        return False
                
        
            
        
    
        
    