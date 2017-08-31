import io
import itertools


def read_literal(literal, width=None, height=None):
    r"""
    Parse a GOL board from a literal to a nested list representation

    :param literal: a GOL board literal
    :param width: number of columns to enforce
    :param height: number of rows to enforce
    :return: nested list representation of the GOL board
    :rtype: list[list[bool]]

    A literal is a plain string, with rows separated by newlines. Every
    character is a field of the GOL board, and any non-empty character
    counts as alive. The use of long strings is recommended, but not required.
    The following literals produce the same board::

    .. code

        long_string = \"\"\"\\
             1
        ABC  2  DEF
             3
        \"\"\"\

        short_string = '     #     \nXXX  #  XXX\n     #     \n'

    The result is a nested list of lists, which can be indexed as ``matrix[row][column]``.
    In other words, the first index is the height and the second the width when viewed as a literal.
    Any field has a value of :py:const:`True` if it is alive, and :py:const:`False` otherwise.
    For the above literals, the following matrix is generated::

    .. code::

        [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    The parameters ``width`` and ``height`` allow to shrink or expand the GOL board:
    Any row is trimmed or filled with :py:const:`False` to the length of ``width``.
    No more than ``height`` rows are returned, and empty rows are appended if the literal is too short.

    If any of ``width`` or ``height`` is :py:const:`None` (the default), it is computed to match
    the biggest extends of the literal.
    Note that specifying ``height`` but not ``width`` means that skipped rows are not inspected to
    derive ``width``.
    """
    if width is None:
        buffer = _read_unbounded_literal(literal, height)
        width = len(buffer[0]) if buffer else 0
    else:
        buffer = _read_bounded_literal(literal, width, height)
    if height is not None:
        if len(buffer) < height:
            buffer.extend(
                [[0] * width] * (height - len(buffer))
            )
    return buffer


def _parse_literal(literal, height):
    for line in itertools.islice(io.StringIO(literal), height):
        yield [char != ' ' for char in line if char != '\n']


def _read_bounded_literal(literal, width, height):
    buffer = []
    for line in _parse_literal(literal, height):
        line = line[:width]
        line += [0] * (width - len(line))
        buffer.append(line)
    return buffer


def _read_unbounded_literal(literal, height):
    buffer = []
    for line in _parse_literal(literal, height):
        buffer.append(line)
    if not buffer:
        return buffer
    width = max(len(line) for line in buffer)
    for line_idx in range(len(buffer)):
        buffer[line_idx].extend([0] * (width - len(buffer[line_idx])))
    return buffer
