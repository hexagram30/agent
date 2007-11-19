import curses
from math import sqrt
from time import sleep

class ObjectPlacementError(Exception):
    pass

class Location(object):
    """

    """
    def __init__(self, x, y, z, *coords):
        if coords:
            x, y, z = coords
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        if (self.x == other.x and self.y == other.y and self.z == other.z):
            return True
        return False

    def __sub__(self, other):
        assert(isinstance(other, Location))
        x = (self.x - other.x)**2
        y = (self.y - other.y)**2
        z = (self.z - other.z)**2
        return sqrt(abs(x + y + z))

    def __repr__(self):
        return "<%s: x=%s, y=%s, z=%s>" % (
            self.__class__.__name__, self.x, self.y, self.z)

    def __call__(self):
        return (self.x, self.y, self.z)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def getCoords(self):
        return (self.x, self.y, self.z)


class Place(object):
    """

    """
    def __init__(self, w=1, l=1, h=1):
        self.width = w
        self.length = l
        self.height = h
        self.area = w * l
        self.volume = w * l * h
        self.map = {}

    def __contains__(self, objOrLocation):
        """

        """
        if isinstance(objOrLocation, Location):
            x, y, z = objOrLocation()
            # the ranges we need to check are, for example, from 1 to width. In
            # other words, we're not looking for indices, but rather positive
            # quanta in a grid.
            if (x in xrange(1, self.width+1) and y in xrange(1, self.length+1)
                and z in xrange(1, self.height+1)):
                return True
            return False
        elif isinstance(objOrLocation, Object):
            if objOrLocation in self.map.values():
                return True
            return False
        else:
            msg = "A Place object can only check for locations or objects."
            raise Exception, msg

    def __repr__(self):
        return "<%s: w=%s, l=%s, h=%s>" % (
            self.__class__.__name__, self.width, self.length, self.height)

    def addObject(self, obj, location):
        """

        """
        # update map
        if isinstance(location, tuple):
            location = Location(*location)
        if location not in self:
            msg = "Can't add an object at a non-location."
            raise Exception, msg
        self.map[location] = obj
        obj.location = location
        obj.setContainer(self)

    def getObjectAt(self, location):
        """

        """
        return self.map[location]

    def moveObject(self, obj, location):
        """

        """
        oldLoc = None
        if obj not in self.map.values():
            msg = "Cannot move something that's not there!"
            raise Exception, msg
        if location in self.map.keys():
            msg = "Something's already there!"
            raise ObjectPlacementError, msg
        for loc, o in self.map.items():
            if o == obj:
                oldLoc = loc
                break
        #print "Leaving %s for %s..." % (oldLoc, location)
        self.map[oldLoc] = None
        self.map[location] = obj
        obj.location = location


class Room(Place):
    pass


class CursesRoom(Room):
    """

    """
    def __init__(self, *args, **kwds):
        super(CursesRoom, self).__init__(*args, **kwds)
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        padX = 5
        padY = 3
        self.canvas = curses.newwin(self.length+2, self.width+3, padY, padX)

    def addChar(self, x, y, char):
        try:
            self.canvas.addch(y, x, ord(char))
            self.canvas.refresh()
        except:
            pass

    def clearChar(self, x, y):
        self.addChar(x, y, ' ')

    def drawBorder(self):
        for x in xrange(self.width+2):
            for y in xrange(self.length+2):
                if (y == 0 or y == self.length+1):
                    self.addChar(x, y, '=')
                elif (x == 0 or x == self.width+1):
                    self.addChar(x, y, '|')

    def destroy(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        
        
class Relationship(dict):
    """

    """
    def __init__(self, owner, obj, attraction):
        """

        """
        self.owner = owner
        self.object = obj
        self.attraction = attraction

    def getObjectDistance(self, location=None):
        if not location:
            location = self.owner.location
        return location - self.object.location

    def getDistances(self):
        possibilities = self.owner.getNeighboringLocations()
        distances = [(self.getObjectDistance(x), x) for x in possibilities]
        distances.sort()
        return distances

    def getNearestAdjacentLocation(self):
        """
        Examine all neighboring locations and find the one that is closest to
        the object in this relationship.
        """
        return self.getDistances()[0][1]

    def getFurthestAdjacentLocation(self):
        return self.getDistances()[-1][1]

class Object(object):
    pass


class Person(Object):
    """

    """
    def __init__(self, id, container=None, location=(), relationships={}):
        """

        """
        self.id = self.name = id
        self.container = container
        if location and isinstance(location, tuple):
            location = Location(*location)
        self.location = location
        self.relationships = relationships

    def setContainer(self, container):
        self.container = container

    def addRelationship(self, relationship):
        """

        """
        assert(relationship.owner == self)
        self.relationships[relationship.object] = relationship

    def step(self, location):
        try:
            self.container.moveObject(self, location)
            return True
        except ObjectPlacementError:
            return False

    def getNeighboringLocations(self):
        """

        """
        locations = []
        assert(self.location)
        coords = list(self.location())
        for index, coord in enumerate(self.location):
            for change in [-1, 1]:
                coords = list(self.location())
                coords[index] = coords[index] + change
                newLoc = Location(*coords)
                if newLoc in self.container:
                    locations.append(Location(*coords))
        return locations


def runTest():
    print "Testing mildly unrequited love..."
    room = Room(w=20, l=10, h=2)
    alice = Person('alice')
    bob = Person('bob')
    room.addObject(alice, (1,1,1))
    room.addObject(bob, (20,10,1))
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, 1)
    bob.addRelationship(bobToAlice)
    # alice is ambivalent to bob
    aliceToBob = Relationship(alice, bob, 0)
    alice.addRelationship(aliceToBob)
    print "Alice: ", alice.location
    print "Bob: ", bob.location
    print "Distance: ", bob.relationships[alice].getObjectDistance()
    # let's get bob moving
    while bob.location not in alice.getNeighboringLocations():
        loc = bob.relationships[alice].getNearestAdjacentLocation()
        bob.step(loc)
    print "Alice: ", alice.location
    print "Bob: ", bob.location
    print "Distance: ", bob.relationships[alice].getObjectDistance()

def setupRoom():
    room = CursesRoom(w=20, l=10, h=2)
    room.drawBorder()
    alice = Person('alice')
    room.addObject(alice, (1,1,1))
    room.addChar(1, 1, 'A')
    bob = Person('bob')
    room.addObject(bob, (20,10,1))
    room.addChar(20, 10, 'B')
    return room, alice, bob

def bobSeeksAlice():
    room, alice, bob = setupRoom()
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, 1)
    bob.addRelationship(bobToAlice)
    # alice is ambivalent to bob
    aliceToBob = Relationship(alice, bob, 0)
    alice.addRelationship(aliceToBob)
    # let's get bob moving
    while bob.location not in alice.getNeighboringLocations():
        sleep(0.25)
        loc = bob.relationships[alice].getNearestAdjacentLocation()
        room.addChar(bob.location.x, bob.location.y, '.')
        bob.step(loc)
        room.addChar(loc.x, loc.y, 'B')
    room.destroy()

def bobAndAliceSeek():
    room, alice, bob = setupRoom()
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, 1)
    bob.addRelationship(bobToAlice)
    # alice is ambivalent to bob
    aliceToBob = Relationship(alice, bob, 1)
    alice.addRelationship(aliceToBob)
    # let's get bob moving
    while bob.location not in alice.getNeighboringLocations():
        sleep(0.25)
        # walk bob
        bobLoc = bob.relationships[alice].getNearestAdjacentLocation()
        room.addChar(bob.location.x, bob.location.y, 'b')
        if bob.step(bobLoc):
            room.addChar(bobLoc.x, bobLoc.y, 'B')
        else:
            room.addChar(bob.location.x, bob.location.y, 'B')
        # walk alice
        aliceLoc = alice.relationships[bob].getNearestAdjacentLocation()
        room.addChar(alice.location.x, alice.location.y, 'a')
        if alice.step(aliceLoc):
            room.addChar(aliceLoc.x, aliceLoc.y, 'A')
        else:
            room.addChar(alice.location.x, alice.location.y, 'A')
    room.destroy()

def aliceSeeksBobHarder():
    room, alice, bob = setupRoom()
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, 1)
    bob.addRelationship(bobToAlice)
    # alice is ambivalent to bob
    aliceToBob = Relationship(alice, bob, 2)
    alice.addRelationship(aliceToBob)
    # let's get bob moving
    while alice.location not in bob.getNeighboringLocations():
        sleep(0.25)
        for t in xrange(aliceToBob.attraction):
            # walk alice
            aliceLoc = alice.relationships[bob].getNearestAdjacentLocation()
            room.addChar(alice.location.x, alice.location.y, 'a')
            if alice.step(aliceLoc):
                room.addChar(aliceLoc.x, aliceLoc.y, 'A')
            else:
                room.addChar(alice.location.x, alice.location.y, 'A')
        # walk bob
        bobLoc = bob.relationships[alice].getNearestAdjacentLocation()
        room.addChar(bob.location.x, bob.location.y, 'b')
        if bob.step(bobLoc):
            room.addChar(bobLoc.x, bobLoc.y, 'B')
        else:
            room.addChar(bob.location.x, bob.location.y, 'B')

    room.destroy()

def bobAvoidsAlice():
    room, alice, bob = setupRoom()
    # bob is interested in being closer to alice
    bobToAlice = Relationship(bob, alice, -1)
    bob.addRelationship(bobToAlice)
    # alice is ambivalent to bob
    aliceToBob = Relationship(alice, bob, 1)
    alice.addRelationship(aliceToBob)
    # let's get bob moving
    counter = 0
    while alice.location not in bob.getNeighboringLocations():
        sleep(0.25)
        # walk alice
        aliceLoc = alice.relationships[bob].getNearestAdjacentLocation()
        room.addChar(alice.location.x, alice.location.y, 'a')
        if alice.step(aliceLoc):
            room.addChar(aliceLoc.x, aliceLoc.y, 'A')
        else:
            room.addChar(alice.location.x, alice.location.y, 'A')
        # walk bob
        bobLoc = bob.relationships[alice].getFurthestAdjacentLocation()
        room.addChar(bob.location.x, bob.location.y, 'b')
        if bob.step(bobLoc):
            room.addChar(bobLoc.x, bobLoc.y, 'B')
        else:
            room.addChar(bob.location.x, bob.location.y, 'B')
        counter += 1
        if counter > 100:
            break

    room.destroy()

def runCursesTest():
    bobSeeksAlice()
    sleep(1)
    bobAndAliceSeek()
    sleep(1)
    aliceSeeksBobHarder()
    sleep(1)
    bobAvoidsAlice()

if __name__ == '__main__':
    runCursesTest()
