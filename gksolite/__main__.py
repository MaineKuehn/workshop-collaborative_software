import sys
import argparse
import time

from . import patterns
from . import reader
from . import boards
from . import render

try:
    import pyximport
except ImportError:
    pass
else:
    pyximport.install()


def board_help():
    max_pattern_len = max(len(pat) for pat in patterns.PATTERNS)
    print('Specify either an existing pattern or a new board', file=sys.stderr)
    print('Patterns:', file=sys.stderr)
    for index in range(0, len(patterns.PATTERNS), 3):
        print(
            '\t', '  '.join(elem.ljust(max_pattern_len) for elem in patterns.PATTERNS[index:index + 3]),
            file=sys.stderr
        )


def load_board(board_name, *padding):
    if not board_name:
        board_help()
        raise ValueError
    cli_arg_map = {kwarg[0]: kwarg for kwarg in ('top', 'bottom', 'left', 'right')}
    kwargs = {}
    for pad in padding:
        if pad[0] not in cli_arg_map:
            val = float(pad) if pad == 'inf' else int(pad)
            kwargs = {kwarg: val for kwarg in cli_arg_map.values()}
        else:
            direction, amount = pad[0], pad[1:]
            kwargs[cli_arg_map[direction]] = float(amount) if amount == 'inf' else int(amount)
    board_literal = getattr(patterns, board_name, board_name)
    raw_board = reader.read_literal(board_literal)
    return boards.PaddedBoard(raw_board, **kwargs)


def load_gol(module_name):
    __import__(module_name)
    return sys.modules[module_name].GOL


def main(options):
    board = load_board(options.board, *options.padding)
    gol_class = load_gol(options.gol_class)
    gol = gol_class(board)
    display = getattr(render, options.renderer)()
    display.show(gol)
    start_time = time.time()
    _delay, _generations, _every = options.delay, options.generations, options.every
    for generation in range(_generations):
        time.sleep(_delay)
        gol.advance()
        if generation % _every == 0:
            display.show(gol, title='%d/%d %6.3f' % (generation, _generations, (100 / (time.time() - start_time))))
        if generation % 100 == 99:
            print('%10d' % generation, '%6.3f' % (100 / (time.time() - start_time)), 'FPS')
            start_time = time.time()


CLI = argparse.ArgumentParser('')
CLI.add_argument(
    '-c', '--class',
    dest='gol_class',
    help='GOL implementation',
    default='gksol.sparse',
)
CLI_BOARD = CLI.add_argument_group('Board settings')
CLI_BOARD.add_argument(
    '-b', '--board',
    help='Initial board pattern [%(default)s]',
    default='PENTOMINO',
)
CLI_BOARD.add_argument(
    '-p', '--padding',
    help='Padding for all sides as "23" or [tblr] direction as "r23"',
    nargs='*',
    default=['20', 'l40', 'r40'],
)
CLI_SIM = CLI.add_argument_group('Simulation settings')
CLI_SIM.add_argument(
    '-g', '--generations',
    help='Generations to simulate',
    type=int,
    default=100,
)
CLI_SIM.add_argument(
    '-d', '--delay',
    help='Delay between generations',
    type=float,
    default=0.0,
)
CLI_SHOW = CLI.add_argument_group('Display settings')
CLI_SHOW.add_argument(
    '-r', '--renderer',
    help='renderer to display the board',
    choices=render.__all__,
    default='TextDisplay',
)
CLI_SHOW.add_argument(
    '-e', '--every',
    help="Show only every e'th frame",
    default=1,
    type=int,
)

main(CLI.parse_args())
