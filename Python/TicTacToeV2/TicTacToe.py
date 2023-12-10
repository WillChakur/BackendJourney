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
        
class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
    
    def __str__(self):
        return f'Name: {self.name} // Marker: {self.marker}'
    
    def make_move(self, row, col, board):
        board.set_marker(row, col, self.marker)        

def input_verification(game_board):
    positions = [1, 2, 3]
    
    while True:
        try:
            input1 = int(input('Enter the row: '))
            input2 = int(input('Enter the column: '))
        except ValueError:
            print('Please enter integer values for row and column.')
            continue

        if input1 not in positions or input2 not in positions:
            print('Row and Column must be between 1 and 3.')
            continue

        if not game_board.is_empty(input1 - 1, input2 - 1):
            print('Already marked, try another one.')
            continue

        break

    return input1, input2

def main():
    game_board = Board()
    
    p1_name = input("Enter the player 1 name: ")
    p2_name = input("Enter the player 2 name: ")
    
    p1 = Player(p1_name, 'X')
    p2 = Player(p2_name, 'O')
    round = 1
    while True:      
        print()
        print(f'{p1.name} turn.')
        print()
        
        game_board.display()
        
        (p_move_row, p_move_col) = input_verification(game_board)        
        
        p1.make_move(p_move_row - 1, p_move_col - 1, game_board)
        
        if game_board.is_winner(p1):
            print(f'Congrats {p1.name} you have won!!')
            game_board.display()
            break
        
        if game_board.is_full():
            print('We have a draw.')
            game_board.display()
            break
        
        print()
        print(f'{p2.name} turn.')
        print()
        
        game_board.display()
        
        (p_move_row, p_move_col) = input_verification(game_board)  
        
        p2.make_move(p_move_row - 1, p_move_col -1, game_board)
        
        if game_board.is_winner(p2):
            print(f'Congrats {p2.name} you have won!!')
            game_board.display()
            break
        
        if game_board.is_full():
            print('We have a draw.')
            game_board.display()
            break
        
        
        
if __name__ == '__main__':
    main()

            
        