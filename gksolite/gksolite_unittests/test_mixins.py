import unittest
import gksolite.patterns
import gksolite.boards
import gksolite.plain
import random


class Mixin(object):
    """Container class to shield Mixins from top level namespace where ``unittest`` would run them"""
    class GolMixin(unittest.TestCase):
        """Standard tests for the Game of Life board interface"""
        gol_cls = gksolite.plain.ListGol

        @staticmethod
        def _gol_to_list(gol_board):
            return [[gol_board[line][row] for row in range(gol_board.width)] for line in range(gol_board.height)]

        def test_init_lists(self):
            """initialize with nested list [[0, 1, ...], [1, 0, ...], ...]"""
            for board in (
                [[1, 1], [1, 1]],
                [[0 for _ in range(4)], [0, 1, 1, 0], [0, 1, 1, 0], [0 for _ in range(4)]],
                [[random.randint(0, 1) for _ in range(12)]for _ in range(18)],
            ):
                with self.subTest(board=board):
                    self.assertIsInstance(self.gol_cls(board), self.gol_cls)

        def test_init_board(self):
            """initialize with gmksolite.boards.PaddedBoard"""
            for pattern_name in gksolite.patterns.PATTERNS:
                for padding in ({}, {'top': 20}, {'left': 30}, {'top': 10, 'bottom': 12, 'left': 15, 'right': 37}):
                    board = gksolite.boards.PaddedBoard(
                        getattr(gksolite.patterns, pattern_name),
                        **padding
                    )
                    self.assertIsInstance(self.gol_cls(board), self.gol_cls)

        def test_getitem(self):
            """fetch fields from board by gol[line][row]"""
            for board in (
                [[1, 1], [1, 1]],
                [[0 for _ in range(4)], [0, 1, 1, 0], [0, 1, 1, 0], [0 for _ in range(4)]],
                [[random.randint(0, 1) for _ in range(12)]for _ in range(18)],
            ):
                with self.subTest(board=board):
                    instance = self.gol_cls(board)
                    self.assertEqual(
                        [[instance[line][row] for row in range(len(board[0]))] for line in range(len(board))],
                        board
                    )
                    self.assertEqual(
                        self._gol_to_list(instance),
                        board
                    )

        def test_advance(self):
            """Correct result when advancing"""
            for stable_board in (
                    [[1, 1], [1, 1]],
                    [[0, 0], [0, 0]],
                    [[0 for _ in range(4)], [0, 1, 1, 0], [0, 1, 1, 0], [0 for _ in range(4)]],
            ):
                instance_block = self.gol_cls(stable_board)
                for generation in range(10):
                    instance_block.advance()
                    self.assertEqual(self._gol_to_list(instance_block), stable_board)
