from docopt import docopt
import cli

docstring = cli.__doc__
arguments = docopt(docstring)


def add():
    sum = int(arguments['<x>']) + int(arguments['<y>'])
    print sum
