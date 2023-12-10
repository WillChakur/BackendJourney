class Board:
    def __init__(self):
        self.game_board = [['-', '-', '-'],
                           ['-', '-', '-'],
                           ['-', '-', '-']]
        
    def display(self):
        print(self.game_board[0])
        print()
        print(self.game_board[1])
        print()
        print(self.game_board[2])
    
    def is_empty(self, row, col):
        if self.game_board[row][col] == '-':
            return True
        else:
            return False
        
    def is_full(self):
        for r in range(3):
            for c in range(3):
                if self.game_board[r][c] == '-':
                    return False        
        return True
       
    def verify_rows(self, row, marker):
        for c in range(3):
            if self.game_board[row][c] != marker:
                return False
        return True
        
    def verify_columns(self, col, marker):
        for r in range(3):
            if self.game_board[r][col] != marker:
                return False
        return True    
    
    def verify_diagonal_1(self, marker):
        for n in range(3):
            if self.game_board[n][n] != marker:
                return False
            
        return True
    
    def verify_diagonal_2(self, marker):
        for n in range(3):
            if self.game_board[n][2-n] != marker:
                return False
            
        return True
             
    def is_winner(self, player):
        #Verify rows
        for r in range(3):
            if self.verify_rows(r, player.marker):
                return True
        
        #Verify columns
        for c in range(3):
            if self.verify_columns(c, player.marker):
                return True
            
        #Verify diagonals
        if self.verify_diagonal_1(player.marker):
            return True
        
        if self.verify_diagonal_2(player.marker):
            return True   
        
        return False    
            
    def set_marker(self, row, col, marker):
        if self.is_empty(row, col):
            self.game_board[row][col] = marker
            return True
        else:
            return False