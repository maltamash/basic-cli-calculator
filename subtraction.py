from docopt import docopt
import calc

docstring = calc.__doc__
arguments = docopt(docstring)

def minus():
    minus = int(arguments['<x>']) - int(arguments['<y>'])
    print minus
