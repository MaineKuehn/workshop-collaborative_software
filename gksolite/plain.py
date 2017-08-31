class ListGol(object):
    """
    Game of Life implemented via lists

    :param board: the initial state of the board
    :type board: :py:class:`gksol.boards.PaddedBoard` or List[List[int]]

    .. describe:: gol[n]

        Return the ``n``'th row of the board as a list-like view.
    """
    def __init__(self, board):
        self._board = board
        self.height = len(board)
        self.width = len(board[0]) if board else 0

    def advance(self):
        """Advance the board to the next generation"""
        # most of the board will be empty, so efficiently initialize to that
        next_board = [[0] * self.width for _ in range(self.height)]
        for w in range(self.width):
            for h in range(self.height):
                neighbours = self._neighbours(h, w)
                if neighbours == 3:
                    next_board[h][w] = 1
                elif neighbours == 2:
                    next_board[h][w] = self._board[h][w]
        self._board = next_board

    def _neighbours(self, h, w):
        if h == 0:
            h_indizes = (0, 1)
        elif h == self.height - 1:
            h_indizes = (h - 1, h)
        else:
            h_indizes = (h - 1, h, h + 1)
        if w == 0:
            w_indizes = (0, 1)
        elif w == self.width - 1:
            w_indizes = (w - 1, w)
        else:
            w_indizes = (w - 1, w, w + 1)
        return sum(
            self._board[i][j]
            for i in h_indizes
            for j in w_indizes
            if i != h or j != w
        )

    def __getitem__(self, item):
        return self._board[item]

    def __iter__(self):
        yield from self._board

    def get_matrix(self):
        """Return the game board as a nested list"""
        return [line[:] for line in self._board]

GOL = ListGol
