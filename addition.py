from docopt import docopt
import test

docstring = test.__doc__
arguments = docopt(docstring)


def add():
    sum = int(arguments['<x>']) + int(arguments['<y>'])
    print sum
