from __future__ import annotations
from urwid import WidgetDecoration, WidgetWrap, Text, Columns, Pile, Filler
from oresat_tpane import TextFill


class DataGrid(WidgetWrap):

    def __init__(self, data: list[tuple], headers: tuple, keys: tuple = None):
        if keys is None:
            self.keys = []
        else:
            self.keys = keys
        self.index = {}
        self.table = []
        header_widgets = []
        for header in headers:
            header_widgets.append(Text(header))
            if keys is None:
                self.keys.append(True)

        if keys is None:
            self.keys = tuple(self.keys)

        self.table.append(Columns(header_widgets))

        for item in data:
            row = []
            key = []
            for i in range(0, len(item)):
                row.append(Text(item[i]))
                if self.keys[i]:
                    key.append(item[i])

            row = Columns(row)
            self.index[tuple(key)] = row
            self.table.append(row)

        self.view = Filler(Pile(self.table), 'top')

        WidgetWrap.__init__(self, self.view)

    def add(self, data: tuple) -> None:
        row = []
        key = []
        for i in range(0, len(data)):
            if self.keys[i]:
                key.append(data[i])
            row.append(Text(data[i]))

        key = tuple(key)
        old = self.index.get(key, None)
        if old is None:
            row = Columns(row)
            self.index[key] = row
            self.table.append(row)
        else:
            old.widget_list = row

        self.view.original_widget = Pile(self.table)

    def __add__(self, data: tuple) -> None:
        self.add(data)

    def __iadd__(self, data: tuple) -> DataGrid:
        self.add(data)
        return self
