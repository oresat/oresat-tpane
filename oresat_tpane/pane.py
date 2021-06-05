import urwid
from urwid.display_common import _BOLD
from urwid.widget import TOP

# New Pane Class as the overall window for Tpane
class Pane():

    # Creates a function to create a new pane
    def new_pane(self):

        # Palette is a created list to be able to choose styling options for different parts of urwid
        palette = [
            ('header', 'white,bold', ''),
        ]

        # Creates a function to close the application
        def exit_on_f10_input(key):
            if key in ('f10', 'F10'):
                urwid.ExitMainLoop()
        
        txt = urwid.Text(('header', u"Oresat Tpane"))
        fill = urwid.Filler(txt, 'top')
        loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_f10_input)
        loop.run()

pane = Pane()
pane.new_pane()