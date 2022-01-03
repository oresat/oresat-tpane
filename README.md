# Terminal Pane

[![license](https://img.shields.io/github/license/oresat/oresat-tpane)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/oresat-tpane)](https://pypi.org/project/oresat-tpane)
[![code-ql](https://img.shields.io/github/workflow/status/oresat/oresat-tpane/Code%20Quality?label=code%20quality)](https://github.com/oresat/oresat-tpane/actions/workflows/codeql-analysis.yml)
[![bugs](https://img.shields.io/github/issues/oresat/oresat-tpane/bug?label=bugs)](https://github.com/oresat/oresat-tpane/labels/bug)
[![unit tests](https://img.shields.io/github/workflow/status/oresat/oresat-tpane/Unit%20Tests?label=unit%20tests)](https://github.com/oresat/oresat-tpane/actions/workflows/unit-tests.yml)
[![deployment](https://img.shields.io/github/workflow/status/oresat/oresat-tpane/Deploy%20to%20PyPi?label=deployment)](https://github.com/oresat/oresat-tpane/actions/workflows/deployment.yaml)
[![feature requests](https://img.shields.io/github/issues/oresat/oresat-tpane/feature%20request?color=purple&label=feature%20request)](https://github.com/oresat/oresat-tpane/labels/feature%20request)

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
