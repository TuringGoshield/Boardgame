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
                    bd_str = bd_str + piece.__repr__() 
                else:
                    bd_str = bd_str + ' '
                bd_str = bd_str + ' |' 

            bd_str = bd_str + '\n'
            bd_str = bd_str + separator_row
        return bd_str

    def on_square(self, loc):
        """Return the piece on a specific square, or list of pieces if more than one."""
        return self._board[loc[0]][loc[1]]

    def place_piece(self, loc, piece):
        """Place a piece on a specific location."""


class Piece:
    def __init__(self):
        """Create a new piece"""

print(Board(3, 3))