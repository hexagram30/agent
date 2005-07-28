from zope.interface import Interface, implements

from interfaces import ICell, IWater, ISlope

class Cell(object):
    implements(ICell)

    def __init__(self, coord_tuple):
        self.coordinates = coord_tuple

class Grassland(Cell):
    pass

class Water(Cell):
    implements(IWater)

class Ocean(Water):
    depth = '100'
    potable = False
    viscosity = 0

class Lake(Water):
    depth = '25'
    potable = True
    viscosity = 0

class Marsh(Water):
    depth = '2'
    potable = False
    viscosity = 0.5

class Slope(Cell):
    implements(ISlope)

class Foothill(Slope):
    grade = '0.05'
    altitude_range = (0, 500)

class Mountain(Slope):
    grade = '0.15'
    altitude_range = (500, 5000)

class TallPeak(Slope):
    grade = '0.35'
    altitude_range = (5000, 8000)

