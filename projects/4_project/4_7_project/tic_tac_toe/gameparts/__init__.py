# gameparts/__init__.py.

# Точка в записи означает текущий каталог.
from .parts import Board
from .exceptions import FieldIndexError
from .exceptions import CellOccupiedError

# чтобы показывало что Board используется в данном каталоге
a = Board
b = FieldIndexError
c = CellOccupiedError
