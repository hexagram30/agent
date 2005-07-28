from adytum import urwid
from adytum.urwid import curses_display
from map import Map, Grid
import time

ui = curses_display.Screen()

AFTER_IMAGE_DELAY = 0.075
VERT_SCALE_COMPENSATION = 0.1

PERMEABLE = r' n'
IMPERMEABLE = r'/\^.#~'
START_CHAR = 'X'

def loadMap(filename):
    cols, rows = ui.get_cols_rows()
    map = urwid.Text(open(filename).read())
    map = urwid.Filler(map, valign="top")
    map = map.render((cols, rows))
    ui.draw_screen((cols, rows), map)
    return Map(filename=filename, start_char=START_CHAR)

def lookAhead(coords=()):
    x, y = coords
    cell_contents = ui.s.inch(y, x)
    #raise str(cell_contents)
    if cell_contents not in range(255):
        #found = str(cell_contents)
        raise "Non ASCII character found on map..."
    else:
        found = chr(cell_contents)
    #ui.fast_put(0, 0, found)
    return found

def passesRules(char):
    if char in PERMEABLE:
        return True
    elif char in IMPERMEABLE:
        return False
    else:
        return False

def cellTraversable(coords=()):
    found = lookAhead(coords)
    if not passesRules(found):
        return False
    return True

class Person(object):
    def __init__(self, xstart, ystart, screen, rep='p'):
        self.x, self.y = (xstart, ystart)
        self.rep = rep
        self.screen = screen
        self.screen.fast_put(xstart, ystart, rep)
        self.last_direction = None
        self.next_coords = (0,0)
        self.cell_contents = None

    def move(self):
        self.oldx, self.oldy = (self.x, self.y)
        self.x, self.y = self.next_coords
        self.screen.fast_put(self.x, self.y, self.rep)
        time.sleep(AFTER_IMAGE_DELAY)
        self.screen.delete(self.oldx, self.oldy)
        msg = 'Old x: %s\n' % self.oldx
        msg += 'Old y: %s\n' % self.oldy
        msg += 'New x: %s\n' % self.x
        msg += 'New y: %s\n' % self.y
        #self.screen.fast_put(0, 0, msg)

    def changeDirection(self):
        self.screen.delete(self.x, self.y)
        time.sleep(AFTER_IMAGE_DELAY)
        self.screen.fast_put(self.x, self.y, self.rep)

    def moveOrTurn(self, this_dir=None):
        if not cellTraversable(coords=self.next_coords):
            return
        if self.last_direction != this_dir:
            self.changeDirection()
        else:
            if this_dir in ['up', 'down']:
                self.moveVert()
            elif this_dir == 'right':
                self.moveRight()
            else:
                self.move()
        self.last_direction = this_dir
        
    def moveVert(self):
        self.move()
        time.sleep(VERT_SCALE_COMPENSATION)
    
    def moveLeft(self, point=()):
        self.next_coords = point
        self.moveOrTurn(this_dir='left')
 
    def moveUp(self, point=()):
        self.next_coords = point
        self.moveOrTurn(this_dir='up')
    
    def moveDown(self, point=()):
        self.next_coords = point
        self.moveOrTurn(this_dir='down')

    def moveRight(self, point=()):
        self.next_coords = point
        self.oldx, self.oldy = (self.x, self.y)
        if point:
            self.x, self.y = point
        #self.screen.s.move(0,0)
        self.screen.fast_put(self.x, self.y, self.rep)
        #self.screen.s.move(0,0)
        time.sleep(AFTER_IMAGE_DELAY)
        self.screen.s.move(self.oldy, self.oldx-1)
        self.screen.fast_delete(self.oldx, self.oldy)
        #self.screen.s.move(0,0)
        self.screen.fast_put(self.x, self.y, self.rep)
        #self.screen.s.move(0,0)

    def jump(self, multiplier=1):
        jumppath = range(multiplier)
        xo, yo = (self.x, self.y)
        # jump up
        for alt in jumppath:
            self.y -= 1
            self.next_coords = (self.x, self.y)
            self.move()
        # descend
        for alt in jumppath:
            self.y += 1
            self.next_coords = (self.x, self.y)
            self.move()
        self.screen.fast_put(self.x, self.y, self.rep)
        self.screen.s.move(0,0)

def run():
    cols, rows = ui.get_cols_rows()
    map = loadMap('testmap.ascii')
    x = int(cols/2)
    y = int(rows/2)
    me = Person(xstart=x, ystart=y, screen=ui)

    # main event loop
    while 1:
        keypress = None
        while not keypress:
            keypress = ui.get_input()
        for key in keypress:
            a = str(key)
            #ui.put(0, 0, a)
            newx = newy = 0
            if key == 'down':
                newy = me.y + 1
                newx = me.x
                me.rep = 'b'
                me.moveDown((newx, newy))                
            elif key == 'up':
                newy = me.y - 1
                newx = me.x
                me.rep = 'p'
                me.moveUp((newx, newy))                
            elif key == 'left':
                newx = me.x - 1
                newy = me.y
                me.rep = 'q'
                me.moveLeft((newx, newy))                
            elif key == 'right':
                newx = me.x + 1
                newy = me.y
                me.rep = 'p'
                me.moveRight((newx, newy))                
            elif key in ['q', 'Q']:
                return
            elif key == ' ':
                me.jump()
            if newx:
                newpoint = (newx, newy)
                # XXX with a move error, we need to print a message
                # about boundaries or something. But, that requires
                # waiting until we have aUI setup

ui.run_wrapper(run)

