import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def addch(win, y, x, char):
    try:
        win.addch(y, x, ord(char))
        win.refresh()
    except:
        pass

beginX = 5
beginY = 5
width = 20
length = 10
win = curses.newwin(length+2, width+3, beginY, beginX)
for x in xrange(width+2):
    for y in xrange(length+2):
        if (y == 0 or y == length+1):
            addch(win, y, x, '=')
        elif (x == 0 or x == width+1):
            addch(win, y, x, '|')

curses.nocbreak()
curses.echo()
curses.endwin()
