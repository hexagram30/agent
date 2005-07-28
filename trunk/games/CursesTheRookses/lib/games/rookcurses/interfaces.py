from zope.interface import Interface, Attribute

class ICell(Interface):
    coordinates = Attribute('''A tuple (x,y) location of the cell on the map.''')
    hitpoints = Attribute('''Hitpoints taken per unit time spent on this cell.''')

class IWater(ICell):
    depth = Attribute('''A cell that is filled with water.''')
    potable = Attribute('''Wheter the water is drinkable or not.''')
    viscosity = Attribute('''The level of the fluid's adhesivness.''')
    
class ISlope(ICell):
    grade = Attribute('''Average slope of the mountain; probably best to
        use this for "level of difficulty" or "technical degree of climb."''')
    altitude_range = Attribute('''A tuple (low, high) of cell heights.''')

