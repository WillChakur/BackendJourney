class TicTacToe():
    def __init__(self):
        game_board = Board()
        player1 = Player("William", "X", game_board)
        player2 = Player("Jackie", "O", game_board)
        
    def show_board(self):
        print game_board.show_board()
        
        