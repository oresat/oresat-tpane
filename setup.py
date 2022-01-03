import setuptools
from oresat_tpane import LIB_NAME, \
                         LIB_VERSION, \
                         LIB_AUTHOR, \
                         MAINTAINER_NAME, \
                         MAINTAINER_EMAIL, \
                         LIB_LICENSE, \
                         LIB_DESCRIPTION, \
                         LIB_DOCS, \
                         LIB_ISSUES, \
                         LIB_URL

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=LIB_NAME,
    version=LIB_VERSION,
    author=LIB_AUTHOR,
    maintainer=MAINTAINER_NAME,
    maintainer_email=MAINTAINER_EMAIL,
    license=LIB_LICENSE,
    description=LIB_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=LIB_URL,
    project_urls={
        'Documentation': LIB_DOCS,
        'Bug Tracking': LIB_ISSUES
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
        "urwid == 2.1.2"
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
