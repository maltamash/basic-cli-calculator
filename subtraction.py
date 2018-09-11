from docopt import docopt
import cli

docstring = cli.__doc__
arguments = docopt(docstring)

def minus():
    minus = int(arguments['<x>']) - int(arguments['<y>'])
    print minus
