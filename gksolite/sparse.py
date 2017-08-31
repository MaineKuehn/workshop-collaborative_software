class SetGol(object):
    """
    Game of Life implemented via sets

    :param board: the initial state of the board
    :type board: :py:class:`gksol.boards.PaddedBoard` or List[List[int]]

    .. describe:: gol[n]

        Return the ``n``'th row of the board as a list-like view.
    """
    def __init__(self, board):
        self.height = len(board)
        self.width = len(board[0]) if board else 0
        self.board = {(h, w) for h in range(self.height) for w in range(self.width) if board[h][w]}

    def advance(self):
        """Advance the board to the next generation"""
        next_board = set()
        for cell in self.board:
            neighbours = self._neighbour_cells(cell)
            # test if current cell survives
            if sum(nb in self.board for nb in neighbours) in {2, 3}:
                next_board.add(cell)
            # test if neighbours are born
            for nb in neighbours:
                if self._valid_cell(nb):
                    if sum(nnb in self.board for nnb in self._neighbour_cells(nb)) == 3:
                        next_board.add(nb)
        self.board = next_board

    @staticmethod
    def _neighbour_cells(cell):
        h, w = cell
        return {
            (h+i, w+j)
            for i in (-1, 0, 1)
            for j in (-1, 0, 1)
            if not i == j == 0
        }

    def _valid_cell(self, cell):
        h, w = cell
        return 0 <= h < self.height and 0 <= w < self.width

    def __iter__(self):
        for idx in range(self.height):
            yield self[idx]

    def __getitem__(self, item):
        return GolRowView(self, item)

    def get_matrix(self):
        """Return the game board as a nested list"""
        return [list(row) for row in self]


class GolRowView(object):
    __slots__ = ('_gol_board', '_row_index')

    def __init__(self, gol_board: SetGol, row_index: int):
        self._gol_board = gol_board
        self._row_index = row_index

    def __len__(self):
        return self._gol_board.width

    def __iter__(self):
        _row_index = self._row_index
        _gol_board = self._gol_board
        for index in range(len(self)):
            yield (_row_index, index) in _gol_board.board

    def __getitem__(self, item):
        return (self._row_index, item) in self._gol_board.board

GOL = SetGol
