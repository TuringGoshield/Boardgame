# Board game structure

class Board:
    """Generic board structure"""
    def __init__(self, height, width):
        self._width = width
        self._height = height
        self._board = [[False for x in range(self._width)]
                       for y in range(self._height)]

    def __repr__(self):

        separator_row = '|'
        for x in range(self._width):
            separator_row = separator_row + '---|'
        separator_row = separator_row + '\n'
        bd_str = separator_row

        for y in range(self._height):
            bd_str = bd_str + '|'
            for x in range(self._width):
                piece = self.on_square((x, y))
                bd_str = bd_str + ' '
                if piece:
                    bd_str = bd_str + str(piece)
                else:
                    bd_str = bd_str + ' '
                bd_str = bd_str + ' |'

            bd_str = bd_str + '\n'
            bd_str = bd_str + separator_row
        return bd_str

    def on_square(self, loc):
        """Return the piece on a specific square, or list of pieces if >1."""
        return self._board[loc[0]][loc[1]]

    def place_piece(self, loc, piece):
        """Place a piece on a specific location."""

        self._board[loc[0]][loc[1]] = piece


class Piece:
    def __init__(self):
        """Create a new piece"""


class tictactoe_Piece(Piece):
    def __init__(self, X=False):
        self.x_or_o = X

    @staticmethod
    def creator(X=False):
        return tictactoe_Piece(X=X)

    def __repr__(self):
        if self.x_or_o:
            return "X"
        else:
            return "O"


class Game:
    def __init__(self, board, make_piece):
        self.board = board
        self.make_piece = make_piece

    def place_piece(self, pos, piece):
        self.board.place_piece(pos, piece)

    def __repr__(self):
        return self.board.__repr__()


TicTacToe = Game(board=Board(3, 3), make_piece=tictactoe_Piece.creator)

TicTacToe.place_piece((0, 0), TicTacToe.make_piece(X=True))

print(TicTacToe)
