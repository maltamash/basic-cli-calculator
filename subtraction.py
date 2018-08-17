from docopt import docopt
import test

docstring = test.__doc__
arguments = docopt(docstring)

def minus():
    minus = int(arguments['<x>']) - int(arguments['<y>'])
    print minus
