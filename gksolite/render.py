import sys
import platform
import atexit


class NullDisplay(object):
    """
    Dummy renderer for a Game of Life board or nested list

    This renderer does nothing.
    """
    def __init__(self, *args):
        pass

    def show(self, gol, title='<Title>'):
        pass


class TextDisplay(object):
    """
    Renderer for a Game of Life board or nested list for text terminals

    :param height: the maximum height to display the board
    :type height: int
    :param width: the maximum width to display the board
    :type width: int

    This renderer requires ANSII support by the terminal.
    """
    def __init__(self, height=128, width=128):
        self.height = height
        self.width = width

    def show(self, gol, title='<Title>'):
        self._show_array(gol, title=title)

    def _show_array(self, gol_array, title):
        sys.stdout.write("\x1b[H")
        draw_width = min(self.width, gol_array.width)
        print('-', title, '-' * max(draw_width - 3 - len(title), 0))
        for h in range(min(self.height, gol_array.height)):
            row = gol_array[h]
            print(''.join('#' if row[w] else ' ' for w in range(min(self.width, gol_array.width))))
        print('-' * gol_array.width)


class NativeMPLDisplay(object):
    """
    Renderer for a Game of Life board or nested list for text terminals

    :param height: the maximum height to display the board
    :type height: int
    :param width: the maximum width to display the board
    :type width: int

    This renderer requires :py:mod:`matplotlib`.
    """
    def __init__(self, height=640, width=640):
        from matplotlib import pyplot
        self.height = height
        self.width = width
        pyplot.draw()

    def show(self, gol, title='<Title>'):
        self._show_mpl(gol, title=title)

    def _show_mpl(self, gol_array, title):
        from matplotlib import pyplot
        draw_height = min(self.height, gol_array.height)
        draw_width = min(self.width, gol_array.width)
        content = []
        for line_idx in range(draw_height):
            line = gol_array[line_idx]
            content.append([line[row_idx] for row_idx in range(draw_width)])
        pyplot.clf()
        pyplot.title(title)
        pyplot.imshow(content)
        pyplot.pause(0.000001)
        
MPLDisplay = NativeMPLDisplay

__all__ = ['TextDisplay', 'MPLDisplay', 'NullDisplay']
