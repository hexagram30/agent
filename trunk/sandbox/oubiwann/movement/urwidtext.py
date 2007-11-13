import urwid
import urwid.curses_display

ui = urwid.curses_display.Screen()

def run():
    txt = urwid.Text('')
    fill = urwid.Filler(txt)
    canvas = fill.render((10, 20))
    ui.draw_screen((10, 20), canvas)

    while not ui.get_input():
        pass

ui.run_wrapper(run)
