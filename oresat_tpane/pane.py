from urwid import WidgetDecoration, WidgetWrap, Text, Divider
from urwid import SolidFill, Widget, Columns, Pile, Filler
from typing import Optional


class VSplit(Columns):
    """ Urwid based vertical split container widget based on the urwid
    Columns class

    Currently this is just the columns class but may be extended or replaced
    in the future"""
    pass


class HSplit(Pile):
    """ Urwid based horizontal split container widget based on the urwid
    Pile class

    Currently this is just the Pile class but may be extended or replaced
    in the future"""
    pass


class TextFill(Filler):
    """Urwid based text widget with fill. This is a convenience widget to
    create the text and filler widget at the same time.

    :ivar text: Reference to the contained text widget
    :type text: Text
    """

    def __init__(self, text: str, valign: str = 'middle', halign: str = 'left'):
        """TextFill Constructor

        :param text: text to be displayed within TextFill
        :type text: str

        :param valign: vertical align text to 'top', 'middle' or 'bottom',
        defaults to 'middle'
        :type valign: str, optional

        :param halign: horizontal align text to 'left', 'right', or 'center',
        defaults to 'left'
        :type halign: str, optional
        """
        self.text = Text(text, halign)
        super().__init__(self.text, valign)


def _format_title(title: str) -> str:
    if len(title) > 0:
        return " %s " % title
    else:
        return ""


def _create_text_widget(text: str, align: str, attr: Optional[str]) \
        -> Optional[Widget]:
    if text == "":
        return None

    if align not in ('left', 'center', 'right'):
        raise ValueError(
            f'align must be one of "left", "right", or "center, {align} '
            f'provided"')

    if attr:
        return Text((attr, _format_title(text)))
    else:
        return Text(_format_title(text))


def _create_header_footer(text: Text, text_align: str, border: bool) \
        -> Optional[Columns]:

    if Text is None and not border:
        return None

    if border:
        line = Divider(u'─')
    else:
        line = Divider(' ')

    if text:
        if text_align == 'left':
            widgets = [('flow', text), line]
        else:
            widgets = [line, ('flow', text)]
            if text_align == 'center':
                widgets.append(line)

    else:
        widgets = [line]

    return Columns(widgets)


class Pane(WidgetDecoration, WidgetWrap):
    """ Urwid based generic pane Widget based on the urwid LineBox class.
    The pane is an urwid box for containing additional urwid based widgets

    :ivar title: reference to the title text widget
    :type title: Text | None

    :ivar footer: reference to the title text widget
    :type footer: Text | None

    :ivar content: content widget encapsulated within pane
    :type content: Widget
    """
    _sizing = frozenset(['box'])
    _selectable = True

    def __init__(self, content: Widget, border: bool = False, title: str = "",
                 title_align: str = "left", title_attr: str = None,
                 footer: str = "", footer_align: str = "left",
                 footer_attr: str = None):
        """Pane Constructor

        :param content: Widget to be displayed within pane
        :type content: Widget

        :param border: 'True' to print border, and 'False' to not print
        border, defaults to 'False'
        :type border: bool, optional

        :param title: Title printed at top of pane, defaults to ""
        :type title: str, optional

        :param title_align: align the title to 'left', 'right', or 'center',
        defaults to 'left'
        :type title_align: str, optional

        :param title_attr: attribute to be assigned to the title text, must
        be included in main loop palette, defaults to None
        :type title_attr: str | None

        :param footer: Footer printed at bottom of pane, defaults to ""
        :type title: str, optional

        :param footer_align: align the footer to 'left', 'right', or 'center',
        defaults to 'left'
        :type title_align: str, optional

        :param footer_attr: attribute to be assigned to the footer text, must
        be included in main loop palette, defaults to None
        :type title_attr: str | None

        :raises ValueError: title_align and footer_align must be valid values
        """

        self.title = _create_text_widget(title, title_align, title_attr)
        self.footer = _create_text_widget(footer, footer_align, footer_attr)

        # Top
        top = _create_header_footer(self.title, title_align, border)

        if border:
            top = Columns([
                ('fixed', 1, Text(u'┌')),
                top,
                ('fixed', 1, Text(u'┐'))
            ])

        # Middle
        self.content = content

        if border:
            middle = Columns([
                ('fixed', 1, SolidFill(u'│')),
                self.content,
                ('fixed', 1, SolidFill(u'│'))
            ])
        else:
            middle = Columns([
                ('fixed', 0, SolidFill(u"")),
                self.content,
            ])

        # Bottom
        bottom = _create_header_footer(self.footer, footer_align, border)

        if border:
            bottom = Columns([
                ('fixed', 1, Text(u'└')),
                bottom,
                ('fixed', 1, Text(u'┘'))
            ])

        pile_widgets = []
        if top:
            pile_widgets.append(('flow', top))
        pile_widgets.append(middle)
        focus_pos = len(pile_widgets) - 1
        if bottom:
            pile_widgets.append(('flow', bottom))

        view = Pile(pile_widgets, focus_item=focus_pos)

        WidgetDecoration.__init__(self, self.content)
        WidgetWrap.__init__(self, view)

    def set_title(self, text: str) -> None:
        """Update the title text (preserves attribute format)

        :param text: New title value
        :type text: str

        :raises ValueError: The title must be initialized with a title to set
        the title

        :return: None
        """
        if not self.title:
            raise ValueError('Cannot set title when not initialized with one')

        if len(self.title.attrib) > 0:
            current_attrib = self.title.attrib[0][0]
        else:
            current_attrib = ""

        self.title.set_text((current_attrib, _format_title(text)))
