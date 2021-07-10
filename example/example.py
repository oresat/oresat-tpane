from datetime import datetime, timedelta
from oresat_tpane import Pane, VSplit, HSplit, TextFill, MainLoop, DataGrid, ExitMainLoop
from time import sleep
from threading import Thread, Event
from random import randint


def delayed_add(grid: DataGrid, event: Event):
    i = 0
    while not event.isSet():
        key = randint(0, 10)
        # grid.add((f"Data{key}", "Data2", f"Data{i}"))
        grid += (f"Data{key}", "Data2", f"Data{i}")
        i += 1
        sleep(1)


def exit_on_q(key):
    raise ExitMainLoop()


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
    headers = ("Header1", "Header2", "Header3")
    data = [
        ("Data1", "Data2", "Data3"),
    ]
    keys = (True, False, False)
    dg = DataGrid(data, headers, keys)
    e = Event()
    thread = Thread(target=delayed_add, args=(dg, e,))
    thread.start()
    hb = Pane(TextFill("Heartbeat", 'top'), True, "Heartbeats: (0 messages)")
    info = Pane(TextFill("Info", 'top'), True, "Info")
    misc = Pane(dg, True, "Miscellaneous: (27 messages)")
    top = VSplit([hb, info])
    container = HSplit([top, misc])

    palette = [("text", "dark blue", 'white')]
    view = Pane(container, False, f'{datetime.now().ctime()},',
                title_attr="text", footer="foot")
    # TODO: exit only works with loop.run
    loop = MainLoop(view, palette, unhandled_input=exit_on_q)
    endtime = datetime.now() + timedelta(minutes=1)
    # Automatically calls loop.stop() when exiting context
    with loop.start():
        while datetime.now() < endtime:
            view.set_title(f'{datetime.now().ctime()},')
            loop.draw_screen()

    e.set()
    thread.join()
