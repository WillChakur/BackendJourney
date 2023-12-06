class Player:
    def __init__(self, name, marker, game_board):
        self.name = name
        self.marker = marker
        self.board = game_board
    
    def get_name(self):
        return self.name
    
    def get_marker(self):
        return self.marker
    
    def make_move(self, Board, row, column):
        if self.board.is_empty(row, column):
            self.board.set_marker(row, column, self.marker)
            
    def __str__(self):
        return f'{self.name} : {self.marker}'
        
    
        
    