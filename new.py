class ChessBoard:
    def __init__(self):
        self.board = [['-' for i in range(8)] for i in range(8)]

    def place_piece(self, piece, row, column):
        self.board[row][column] = piece

    def move_piece(self, from_row, from_column, to_row, to_column):
        piece = self.board[from_row][from_column]
        self.board[from_row][from_column] = '-'
        self.board[to_row][to_column] = piece

    def is_valid(self):
        pass

    def display_board(self):
        for row in self.board:
            print(''.join(row))


chess_board = ChessBoard()
chess_board.place_piece('R', 0, 0)
chess_board.place_piece('H', 0, 1)

chess_board.move_piece(0, 0, 1, 0)
chess_board.display_board()
