import sys
import pytest
import test
from docopt import docopt

doc = test.__doc__

def sum_test():
    args = docopt(doc, ['sum', '1', '2'])
    import addition
    addition = addition.add(args['<x>'], args['<y>'])
    return addition


def test_shit(capsys):
    # print sum_test()
    # captured = capsys.readouterr()
    # print captured.out
    assert sumtest() == '4'

#


#def test_shit(capsys):
    #print(returnsum())
    #captured = capsys.readouterr()
    #assert captured.out == '3\n3\n'


#def sumtest():
    #args = docopt(doc, ['sum', '1', '2'])
    #import addition
    #addition = addition.add(int(args['<x>']), int(args['<y>']))


#def test_myoutput(capsys):  # or use "capfd" for fd-level
    #print("hello")
    #sys.stderr.write("world\n")
    #captured = capsys.readouterr()
    #assert captured.out == "hello\n"
    #assert captured.err == "world\n"
    #print("next")
    #captured = capsys.readouterr()
    #assert captured.out == "next\n"

if __name__ == '__main__':
    pytest.main()
