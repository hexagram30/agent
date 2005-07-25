import urwid.curses_display
import urwid
import time
from copy import copy

ui = urwid.curses_display.Screen()

AFTER_IMAGE_DELAY = 0.075
VERT_SCALE_COMPENSATION = 0.1

class Person(object):
    def __init__(self, xstart, ystart, screen, rep='p'):
        self.x, self.y = (xstart, ystart)
        self.rep = rep
        self.screen = screen
        self.screen.fast_put(xstart, ystart, rep)
        self.last_direction = None

    def move(self, point=()):
        self.oldx, self.oldy = (self.x, self.y)
        if point:
            self.x, self.y = point
        self.screen.fast_put(self.x, self.y, self.rep)
        #self.screen.fast_put(0, 4, 'Put new x & y (%s, %s)' % (self.x, self.y))
        #self.screen.s.move(0,0)
        #self.screen.fast_put(0, 5, 'Put cursor at origin')
        time.sleep(AFTER_IMAGE_DELAY)
        #self.screen.fast_put(0, 6, 'Added delay')
        self.screen.delete(self.oldx, self.oldy)
        #self.screen.fast_put(0, 7, 'Deleted point (%s, %s)' % (self.oldx, self.oldy))
        #self.screen.s.move(0,0)
        #self.screen.fast_put(0, 8, 'Put cursor at origin')
        msg = 'Old x: %s\n' % self.oldx
        msg += 'Old y: %s\n' % self.oldy
        msg += 'New x: %s\n' % self.x
        msg += 'New y: %s\n' % self.y
        #self.screen.fast_put(0, 0, msg)

    def change_direction(self):
        self.screen.delete(self.x, self.y)
        time.sleep(AFTER_IMAGE_DELAY)
        self.screen.fast_put(self.x, self.y, self.rep)

    def move_or_turn(self, point=(), this_dir=None):
        if self.last_direction != this_dir:
            self.change_direction()
        else:
            if this_dir in ['up', 'down']:
                self.move_vert(point=point)
            else:
                self.move(point=point)
        self.last_direction = this_dir
        
    def move_vert(self, point=()):
        self.move(point=point)
        time.sleep(VERT_SCALE_COMPENSATION)
    
    def move_left(self, point=()):
        self.move_or_turn(point=point, this_dir='left')
 
    def move_up(self, point=()):
        self.move_or_turn(point=point, this_dir='up')
    
    def move_down(self, point=()):
        self.move_or_turn(point=point, this_dir='down')

    def move_right(self, point=()):
        if self.last_direction != 'right':
            self.change_direction()
        else:
            self.oldx, self.oldy = (self.x, self.y)
            if point:
                self.x, self.y = point
            self.screen.s.move(0,0)
            self.screen.fast_put(self.x, self.y, self.rep)
            self.screen.s.move(0,0)
            time.sleep(AFTER_IMAGE_DELAY)
            self.screen.s.move(0,0)
            self.screen.fast_delete(self.oldx, self.oldy)
            self.screen.s.move(0,0)
            self.screen.fast_put(self.x, self.y, self.rep)
            self.screen.s.move(0,0)
        self.last_direction = 'right'

    def jump(self, multiplier=1):
        jumppath = range(multiplier)
        xo, yo = (self.x, self.y)
        # jump up
        for alt in jumppath:
            self.y -= 1
            self.move((self.x, self.y))
        # descend
        for alt in jumppath:
            self.y += 1
            self.move((self.x, self.y))
        self.screen.fast_put(self.x, self.y, self.rep)
        self.screen.s.move(0,0)

def run():
    cols, rows = ui.get_cols_rows()

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
                me.move_down((newx, newy))                
            elif key == 'up':
                newy = me.y - 1
                newx = me.x
                me.rep = 'p'
                me.move_up((newx, newy))                
            elif key == 'left':
                newx = me.x - 1
                newy = me.y
                me.rep = 'q'
                me.move_left((newx, newy))                
            elif key == 'right':
                newx = me.x + 1
                newy = me.y
                me.rep = 'p'
                me.move_right((newx, newy))                
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

