class Player():
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
    
    def __str__(self):
        return f'Name: {self.name} // Marker: {self.marker}'
    
    def make_move(self, row, col, board):
        board.set_marker(row, col, self.marker)        

    
        
    