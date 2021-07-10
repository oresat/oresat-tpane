from urwid import WidgetDecoration, WidgetWrap, Text, Columns, Pile, Filler
from oresat_tpane import TextFill


class DataGrid(WidgetWrap):

    def __init__(self, data: list[tuple], headers: list[str]):

        table = []
        header_widgets = []
        for header in headers:
            header_widgets.append(Text(header))

        table.append(Columns(header_widgets))

        for item in data:
            row = []
            for value in item:
                row.append(Text(value))
            table.append(Columns(row))

        self.view = Filler(Pile(table), 'top')

        WidgetWrap.__init__(self, self.view)
