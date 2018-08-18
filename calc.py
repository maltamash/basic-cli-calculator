#!/usr/bin/python
"""
Calculator command line interface tool that just adds shit and minuses it.

Usage:
  calc.py sum <x> <y>
  calc.py minus <x> <y>
  calc.py [--version]
  calc.py [--help]

Options:
  -h --help  Show this page
  -v --version  The version number

"""

from docopt import docopt




if __name__ == '__main__':
    arguments = docopt(__doc__, version="1.0.0")
    if arguments['sum'] is True:
        import addition
        addition.add()
    elif arguments['minus'] is True:
        import subtraction
        subtraction.minus()
