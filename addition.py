from docopt import docopt
import calc

docstring = calc.__doc__
arguments = docopt(docstring)


def add():
    sum = int(arguments['<x>']) + int(arguments['<y>'])
    print sum
