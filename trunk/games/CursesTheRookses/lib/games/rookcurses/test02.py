import curses
import sys

global mymark

args = sys.argv

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

rows, cols = stdscr.getmaxyx()
rows = rows - 2
cols = cols - 2

data = [
    (135,70),
    (92,166),
    (67,35),
    (59,34),
    (24,149),
]

data.sort()
bigx = data[-1][0]
ys = [ y for x,y in data ]
ys.sort()
bigy = ys[-1]
me = ()
mymark = ()

def cleanIt(strtuple):
    st = strtuple.replace('(', '')
    st = st.replace(')', '')
    x,y = st.split(',')
    return (int(x.strip()), int(y.strip()))
'''
if len(args) > 2:
    for arg in args[1:]:
        arg = cleanIt(arg)
        data.append(arg)
else:
    arg = cleanIt(args[1])
    data.append(arg)
'''

def screen2Game(coord):
    x,y = coord
    y = rows - y
    gameX = int(bigx*x/float(cols))
    gameY = int(bigy*y/float(rows))
    return (gameX, gameY)

def game2Screen(coord):
    if isinstance(coord, str):
        coord = cleanIt(coord)
    x,y = coord
    screenX = int(cols*x/float(bigx))
    screenY = rows - int(rows*y/float(bigy))
    return (screenX, screenY)

def drawPoint(point):
    x,y = point
    stdscr.addstr(y, x, '*')
    coords = "(%s,%s)" % screen2Game((x,y))
    clen = len(coords)
    cxstart = x-clen
    cy = y + 1
    stdscr.addstr(cy, cxstart, coords)
    return (point, (cxstart, cy, clen))

class Me(object):
    def __init__(self, point):
        self.point = list(game2Screen(point))
        self.mark = drawPoint(self.point)
        self.x, self.y = self.point
        
    def move(self, point=()):
        if point:
            self.x, self.y = point
        else:
            point = (self.x, self.y)
        oldp, olddata = self.mark
        #raise str(oldp)+str(screen2Game(oldp))
        xo, yo = oldp
        cxstart, cy, clen = olddata
        #stdscr.delch(xo, yo)
        stdscr.delch(yo, xo)
        for i in range(clen):
            stdscr.delch(cy, cxstart + i)
        self.mark = drawPoint(point)
        stdscr.refresh()        

me = Me(args[1])

# now, bigy will be limited by number of rows, and
# bigx will be limited by the number of cols
newdata = [ game2Screen((x,y)) for x,y in data ]
alldata = zip(data,newdata)

txt = "Cols: %s, Rows: %s\n" % (cols, rows)
txt += "Highest x: %s\n" % bigx
txt += "Highest y: %s\n" % bigy
txt += "Orig data: %s\n" % str(data)
txt += "Adj data: %s\n" % str(newdata)

#stdscr.addstr(0,0,txt)

for x,y in newdata:
    drawPoint((x,y))

while 1:
    c = stdscr.getch() 
    old = me
    if c == curses.KEY_DOWN:
        me.y += 1
    elif c == curses.KEY_UP:
        me.y -= 1
    elif c == curses.KEY_LEFT:
        me.x -= 1
    elif c == curses.KEY_RIGHT:
        me.x += 1
    else:
        curses.nocbreak(); 
        stdscr.keypad(0)
        curses.echo()
        curses.endwin()
        break
    me.move()
