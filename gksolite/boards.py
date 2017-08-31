import itertools
from collections import abc as collection_abc


class PaddedBoard(object):
    def __init__(self, board, *, border=0, top=0, bottom=0, left=0, right=0):
        self.board = board
        self.top = top + border
        self.bottom = bottom + border
        self.left = left + border
        self.right = right + border
        self._board_height = len(board)
        try:
            self._board_width = len(board[0])
        except IndexError:
            self._board_width = 0

    @property
    def height(self):
        return self.top + self._board_height + self.bottom

    @property
    def width(self):
        return self.left + self._board_width + self.right

    def __getitem__(self, index):
        if index < 0:
            index += self.height
        if index < 0 or index >= self.height:
            raise IndexError('board height index out of range')
        if index < self.top or index >= self.top + self._board_height:
            return FillerRow(self.width)
        return PaddedRow(self.board[index - self.top], left=self.left, right=self.right)

    def __iter__(self):
        width = self.width
        yield from (FillerRow(width) for _ in range(self.top))
        yield from (PaddedRow(row, left=self.left, right=self.right) for row in self.board)
        yield from (FillerRow(width) for _ in range(self.bottom))

    def __len__(self):
        return self.height
    
    def __str__(self):
        return '[%s]' % ', '.join(str(line) for line in self)


class PaddedRow(collection_abc.Sequence):
    def __init__(self, row, left=0, right=0):
        self.row = row
        self.left = left
        self.right = right

    def __len__(self):
        return self.left + self.right + len(self.row)

    def __iter__(self):
        yield from (0 for _ in range(self.left))
        yield from self.row
        yield from (0 for _ in range(self.right))

    def __getitem__(self, item):
        length = len(self)
        if item < -length or item > length:
            raise IndexError('list index out of range')
        if item < 0:
            item = length - item
        if item < self.left or item >= length - self.right:
            return 0
        return self.row[item - self.left]

    def __repr__(self):
        return '%s(left=%d, right=%d, %r)' % (self.__class__.__name__, self.left, self.right, self.row)

    def __str__(self):
        return '[%s]' % ', '.join(itertools.chain(
            *('0' for _ in range(self.left)),
            [str(self.row)[1:-1]],
            *('0' for _ in range(self.right)),
        ))


class FillerRow(collection_abc.Sequence):
    def __init__(self, length):
        self._length = length

    def __len__(self):
        return self._length

    def __iter__(self):
        yield from (0 for _ in range(self._length))

    def __getitem__(self, item):
        if -self._length < item < self._length:
            return 0
        raise IndexError('list index out of range')
    
    def __repr__(self):
        return "%s(%d)" % (self.__class__.__name__, self._length)

    def __str__(self):
        return '[%s]' % (("0, " * self._length)[:-2])
