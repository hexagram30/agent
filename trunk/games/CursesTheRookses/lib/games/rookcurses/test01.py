import urwid.curses_display
import urwid
import time

ui = urwid.curses_display.Screen()

data = [
    (135,70),
    (92,166),
    (67,35),
    (59,34),
    (24,149),
]

class Me(object):
    def __init__(self, xstart, ystart, screen, rep='p'):
        self.x, self.y = (xstart, ystart)
        self.rep = rep
        self.screen = screen
        self.screen.fast_put(xstart, ystart, rep)
        
    def move(self, point=()):
        oldx, oldy = (self.x, self.y)
        if point:
            self.x, self.y = point
        else:
            point = (self.x, self.y)
        self.screen.delete(oldx, oldy)
        self.screen.fast_put(self.x, self.y, self.rep)

    def jump(self, multiplier=2):
        xo = self.x
        yo = self.y
        jumppath = range(multiplier)
        # jump up
        for alt in jumppath:
            self.y += 1
            self.move((self.x, self.y))
            time.sleep(1) 
        # descend
        for alt in jumppath:
            self.y -= 1
            self.move((self.x, self.y))
            time.sleep(1) 

def run():
    cols, rows = ui.get_cols_rows()

    data.sort()
    bigx = data[-1][0]
    ys = [ y for x,y in data ]
    ys.sort()
    bigy = ys[-1]

    # now, bigy will be limited by number of rows, and
    # bigx will be limited by the number of cols
    newdata = [ (int(cols*x/135.),int(rows*y/166.)) for x,y in data ]

    txt = "Cols: %s, Rows: %s\n" % (cols, rows)
    txt += "Highest x: %s\n" % bigx
    txt += "Highest y: %s\n" % bigy
    txt += "Orig data: %s\n" % str(data)
    txt += "Adj data: %s\n" % str(newdata)
    #txt = urwid.Text(txt)
    #fill = urwid.Filler(txt, valign="top")
    #canvas = fill.render((cols, rows))
    #ui.draw_screen((cols, rows), canvas)

    x = int(cols/2)
    y = int(rows/2)
    me = Me(xstart=x, ystart=y, screen=ui)

    # main event loop
    while 1:
        keypress = None
        while not keypress:
            keypress = ui.get_input()
        for key in keypress:
            newx = newy = 0
            if key == 'down':
                newy = me.y + 1
                newx = me.x
                time.sleep(0.1)
            elif key == 'up':
                newy = me.y - 1
                newx = me.x
                time.sleep(0.1)
            elif key == 'left':
                newx = me.x - 1
                newy = me.y
                me.rep = 'q'
            elif key == 'right':
                newx = me.x + 1
                newy = me.y
                me.rep = 'p'
            elif key in ['q', 'Q']:
                return
            elif key == 'space':
                me.jump()
            if newx:
                newpoint = (newx, newy)
                # XXX with a move error, we need to print a message
                # about boundaries or something. But, that requires
                # waiting until we have aUI setup
                me.move(newpoint)

ui.run_wrapper(run)

