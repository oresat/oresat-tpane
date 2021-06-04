import setuptools
import tpane as t

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=t.LIB_NAME,
    version=t.LIB_VERSION,
    author=t.LIB_AUTHOR,
    maintainer=t.MAINTAINER_NAME,
    maintainer_email=t.MAINTAINER_EMAIL,
    license=t.LIB_LICENSE,
    description=t.LIB_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=t.LIB_URL,
    project_urls={
        'Documentation': t.LIB_DOCS,
        'Bug Tracking': t.LIB_ISSUES
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console :: Curses",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: User Interfaces",
    ],
    install_requires=[
        "urwid >= 2.1.2"
    ],
    extras_require={
        "dev": [
            "python-can",
            "setuptools",
            "wheel",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3.9.0',
)
