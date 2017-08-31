from . import test_mixins
from gksolite import sparse as gol_module


class TestSetGOL(test_mixins.Mixin.GolMixin):
    gol_cls = gol_module.GOL
