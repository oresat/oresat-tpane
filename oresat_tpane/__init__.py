"""This module is responsible for providing a high-level interface for elements
of Curses UI and general user interaction with the app,
"""
from oresat_tpane.pane import Pane, VSplit, HSplit, TextFill
from oresat_tpane.datagrid import DataGrid
from urwid import MainLoop, ExitMainLoop

MAJOR = 0
MINOR = 0
PATCH = 1

LIB_NAME = 'oresat-tpane'
LIB_DESCRIPTION = 'This module is responsible for providing a high-level interface for elements of Curses UI and general user interaction with the app'
LIB_VERSION = f'{MAJOR}.{MINOR}.{PATCH}'
LIB_AUTHOR = 'Dmitri McGuckin'
LIB_EMAIL = 'dmitri3@pdx.edu'
LIB_URL = 'https://github.com/oresat/oresat-tpane'
LIB_LICENSE = 'GPL-3.0'
LIB_DOCS = 'https://canopen-monitor.readthedocs.io'
LIB_ISSUES = 'https://github.com/oresat/oresat-tpane/labels/bug'


MAINTAINER_NAME = 'Portland State Aerospace Society'
MAINTAINER_EMAIL = 'oresat@pdx.edu'

__all__ = [
    "Pane",
    "VSplit",
    "HSplit",
    "TextFill",
    "MainLoop",
    "DataGrid",
]
