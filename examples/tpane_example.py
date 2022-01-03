#!/usr/bin/env python3
from datetime import datetime
from oresat_tpane import Pane, VSplit, HSplit, TextFill, DataGrid
from time import sleep
from threading import Thread, Event
from random import randint


def delayed_add(grid: DataGrid, event: Event):
    i = 0
    while not event.is_set():
        key = randint(0, 10)
        # grid.add((f"Data{key}", "Data2", f"Data{i}"))
        grid += (f"Data{key}", "Data2", f"Data{i}")
        i += 1
        sleep(1)


def update_header(pane: Pane, event: Event):
    while not event.is_set():
        pane.set_title(f'{datetime.now().ctime()},')
        sleep(1)


def force_refresh(main_loop, data=None):
    main_loop.draw_screen()
    main_loop.set_alarm_in(0.2, force_refresh)


def main():
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
    thread2 = Thread(target=update_header, args=(view, e,))
    thread2.start()
    e.set()
    thread.join()
    thread2.join()

if __name__ == '__main__':
    main()
