from __future__ import annotations
from urwid import WidgetWrap, Text, Columns, ListBox, SimpleListWalker, Frame


class DataGrid(WidgetWrap):
    """Urwid based datagrid widget. Used for displaying and updating a table
    of data

    :ivar keys: A key index for accessing rows being displayed.
    :type keys: { tuple: Columns }

    :ivar table: reference to table of displayed rows
    :type table: [Columns]

     :ivar header: header row
     :type header: Columns

     :ivar body: reference to listbox that contains displayed data
     :type body: ListBox

     :ivar view: Widget wrapping everything that is being displayed
     :type view: Frame
     """

    def __init__(self, data: list[tuple], headers: tuple, keys: tuple = None):
        """ Datagrid constructor
        :param data: Initial data to display
        :type data: [tuple]

        :param headers: tuple of header text to display
        :type headers: tuple,

        :param keys: tuple of booleans to indicate keys
        :type keys: tuple | None
        """
        if keys is None:
            self.keys = []
        else:
            self.keys = keys
        self.index = {}
        header_widgets = []
        for header in headers:
            header_widgets.append(Text(header))
            if keys is None:
                self.keys.append(True)

        if keys is None:
            self.keys = tuple(self.keys)

        self.header = Columns(header_widgets)
        self.body = SimpleListWalker([])
        self.table = self.body.contents

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

        listbox = ListBox(self.body)

        self.view = Frame(listbox, header=self.header)

        WidgetWrap.__init__(self, self.view)

    def add(self, data: tuple) -> None:
        """Add record to data table
        :param data: row of data to be added
        :type data: tuple
        """
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

    def __add__(self, data: tuple) -> None:
        """Add record to data table
        :param data: row of data to be added
        :type data: tuple
        """
        self.add(data)

    def __iadd__(self, data: tuple) -> DataGrid:
        """Add record to data table
        :param data: row of data to be added
        :type data: tuple
        """
        self.add(data)
        return self
