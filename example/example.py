from datetime import datetime, timedelta
from oresat_tpane import Pane, VSplit, HSplit, TextFill, MainLoop

if '__main__' == __name__:
    """
    This was my first attempt to create a canopen-monitor type interface 
    using only standard urwid widgets
    
    frame = urwid.Frame(body=urwid.Filler(urwid.Text('HELLO World!')),
                        header=urwid.Text('Header'),
                        footer=urwid.Text('Footer'))

    top = urwid.Columns([frame, frame])
    bottom = urwid.Columns([frame])
    pile = urwid.Pile([top, bottom])
    line = urwid.LineBox(pile, f'{datetime.now().ctime()},', title_align='left',
                         title_attr=None, tlcorner=' ', tline=' ', lline=' ',
                         trcorner=' ', blcorner=' ', rline=' ',
                         bline=' ', brcorner=' ')

    """
    hb = Pane(TextFill("Heartbeat", 'top'), True, "Heartbeats: (0 messages)")
    info = Pane(TextFill("Info", 'top'), True, "Info")
    misc = Pane(TextFill("Misc", 'top'), True, "Miscellaneous: (0 messages)")
    top = VSplit([hb, info])
    container = HSplit([top, misc])

    palette = [("text", "dark blue", 'white')]
    view = Pane(container, False, f'{datetime.now().ctime()},',
                title_attr="text")

    loop = MainLoop(view, palette)
    endtime = datetime.now() + timedelta(minutes=1)
    # Automatically calls loop.stop() when exiting context
    with loop.start():
        while datetime.now() < endtime:
            view.set_title(f'{datetime.now().ctime()},')
            loop.draw_screen()

