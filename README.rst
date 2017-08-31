workshop-collaborative_software
###############################
The provided materials are part of the workshop 'Collaborative Software Development' at the GridKa School 2017.

gksolite
--------

A stripped down version of the Game of Life implemented in the "Advanced Python Programming Course".
The modules ``gksolite.plain`` and ``gksolite.sparse`` provide classes to load and advance a GOL board.
Their interface adheres to:

.. code::

    # initialize a new board from a list
    GOL(board: List[List[int]]) -> gol
    # advance the simulation by one step
    gol.advance() -> None
    # get the current board as a List[List[int]]
    gol.get_matrix()

If you need a new board, you should use three elements:

literals, e.g. from ``gksolite.patterns``
    A string with line-breaks separating lines on the game board.

``gksolite.reader.read_literal``
    Reads a literal to a nested list of type ``List[List[int]]``.

``gksolite.boards.PaddedBoard``
    Pad a nested list to provide more space for a board.

For example, you can load an exponentially growing pattern to a ~200x200 board:

.. code::

    from gksolite import patterns, reader, boards
    board = boards.PadderBoard(
        reader.read_literal(
            patterns.BASELINE
        ),
        border=100
    )
