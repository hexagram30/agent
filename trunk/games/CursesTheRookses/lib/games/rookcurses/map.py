from landforms import Grassland
from landforms import Ocean, Marsh
from landforms import Foothill, Mountain

class AsciiCellParser(object):
    
    def parse(self, cell_rep):
        if cell_rep == ' ':
            cell_object = Grassland
        elif cell_rep in ['/', '\\']:
            cell_object = Mountain
        elif cell_rep == '^':
            cell_object = Foothill
        elif cell_rep == '~':
            cell_object = Ocean
        elif cell_rep == '#':
            cell_object = Marsh
        else:
            raise "There is no object set for represenation '%s'." % cell_rep
        return cell_object
        
class Grid(object):

    def __init__(self, radius=1, origin=()):
        self.width = 0
        self.top_left = ()
        self.setRadius(radius, origin)
        self.origin = origin
        self.object_map = {}
        self.parser = AsciiCellParser()

    def setRadius(self, radius, origin):
        self.radius = radius
        self.origin = origin
        xo, yo = origin
        self.width = (radius * 2) + 1
        self.top_left = (xo-(radius), yo-(radius))

    def populate(self, map):
        xtl, ytl = self.top_left
        # need to do some checks at some point against
        # coords that are off the map; should probably
        # have every coord off the map get components
        # of -1, and then just check in the iteration
        # here if make sure x & y are >= 0.
        for y in range(ytl, self.width+ytl):
            for x in range(xtl, self.width+xtl):
                coords = (x, y)
                print coords
                if 0 <= x <= map.width and 0 <= y <= map.height:
                    # parse this point on the map and
                    # get the type of object it is
                    cell_rep = map.getCellRep((x,y))
                    cell_object = self.parser.parse(cell_rep)
                    # instantiate the object
                    cell_instance = cell_object(coords)

                    # dump into object_map
                    # XXX it would be nice to not have to re-instantiate
                    # objects that are already in the grid; it would be 
                    # much more preferable to shift grid elements one way
                    # or another.
                else: 
                    cell_instance = None
                mapping = {coords:cell_instance}
                self.object_map.update(mapping)

class Map(object):

    def __init__(self, filename='', screen=None, start_char='X'):
        self.filename = filename
        self.screen = screen
        self.start_char = start_char
        self.width = 0
        self.height = 0
        self.load()

    def load(self):
        raw = open(self.filename).read()
        self.rawlines = raw.split('\n')
        self.findStart()

    def findStart(self):
        x = y = 0
        line = ''
        for line in self.rawlines:
            if y == 0:
                self.width = len(line)
            try:
                x = line.index(self.start_char)
                self.start = (x, y)
                # now replace the 'X' (or whatever the marker is)
                # because we don't want to see it in game play
                self.rawlines[y] = line.replace(self.start_char, ' ')
            except ValueError:
                pass
            y += 1
        if not x:
            raise "The ASCII map appears to be invalid; " + \
                "there is no starting point."
        self.height = y

    def getCellRep(self, coords=()):
        x, y = coords
        return self.rawlines[y][x]

    def _calcGrid(self, radius):
        pass

def _test():
    import doctest, map
    return doctest.testmod(map)

if __name__ == '__main__':
    _test()

