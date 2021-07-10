from datetime import datetime, timedelta
from oresat_tpane import Pane, VSplit, HSplit, TextFill, MainLoop, DataGrid

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
    headers = ["Header1", "Header2", "Header3"]
    data = [
        ("Data1", "Data2", "Data3"),
        ("Data2", "Data5", "Data6"),
        ("Data3", "Data5", "Data6"),
        ("Data4", "Data5", "Data6"),
        ("Data5", "Data5", "Data6"),
        ("Data6", "Data5", "Data6"),
        ("Data7", "Data5", "Data6"),
        ("Data8", "Data5", "Data6"),
        ("Data9", "Data5", "Data6"),
        ("Data10", "Data5", "Data6"),
        ("Data11", "Data5", "Data6"),
        ("Data12", "Data5", "Data6"),
        ("Data13", "Data5", "Data6"),
        ("Data14", "Data5", "Data6"),
        ("Data15", "Data5", "Data6"),
        ("Data16", "Data5", "Data6"),
        ("Data17", "Data5", "Data6"),
        ("Data18", "Data5", "Data6"),
        ("Data19", "Data5", "Data6"),
        ("Data20", "Data5", "Data6"),
        ("Data21", "Data5", "Data6"),
        ("Data22", "Data5", "Data6"),
        ("Data23", "Data5", "Data6"),
        ("Data24", "Data5", "Data6"),
        ("Data25", "Data5", "Data6"),
        ("Data26", "Data5", "Data6"),
        ("Data27", "Data5", "Data6"),
    ]
    dg = DataGrid(data, headers)

    hb = Pane(TextFill("Heartbeat", 'top'), True, "Heartbeats: (0 messages)")
    info = Pane(TextFill("Info", 'top'), True, "Info")
    misc = Pane(dg, True, "Miscellaneous: (27 messages)")
    top = VSplit([hb, info])
    container = HSplit([top, misc])

    palette = [("text", "dark blue", 'white')]
    view = Pane(container, False, f'{datetime.now().ctime()},',
                title_attr="text", footer="foot")

    loop = MainLoop(view, palette)
    endtime = datetime.now() + timedelta(minutes=1)
    # Automatically calls loop.stop() when exiting context
    with loop.start():
        while datetime.now() < endtime:
            view.set_title(f'{datetime.now().ctime()},')
            loop.draw_screen()

