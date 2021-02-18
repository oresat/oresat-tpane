# Terminal Pane

[![license](https://img.shields.io/github/license/oresat/CANopen-monitor)](./LICENSE)
[![issues](https://img.shields.io/github/issues/oresat/oresat-tpane/bug)](https://github.com/oresat/oresat-tpane/labels/bug)
<!-- [![pypi]()]() -->
<!-- [![read the docs]()]() -->
<!-- [![unit tests]()]()
[![deployment]()]() -->

A wrapper... to the NCurses library, providing high-level interface to "Panes" and "Windows" allowing for easier development of TUI applications

***

# Quick Start

### Install

`$` `pip install tpane`

***

# Development and Contribution

<!-- ### Documentation

Check out our [Read The Docs](https://oresat-tpane.readthedocs.io) pages for more info on the application sub-components and methods. -->

### Install Locally

`$` `pip install -e .[dev]`

*(Note: the `-e` flag creates a symbolic-link to your local development version. Set it once, and forget it)*

### Create Documentation Locally

`$` `make -C docs clean html`

*(Note: documentation is configured to auto-build with ReadTheDocs on every push to master)*
