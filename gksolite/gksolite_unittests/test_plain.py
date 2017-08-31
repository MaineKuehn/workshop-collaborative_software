from . import test_mixins
from gksolite import plain as gol_module


class TestListGOL(test_mixins.Mixin.GolMixin):
    gol_cls = gol_module.GOL
