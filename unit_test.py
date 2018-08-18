import unittest
from docopt import docopt
import calc

doc = calc.__doc__

class testingthecli(unittest.TestCase):
    def testfor_versioninput(self): #testing for input values
        argv = ['--version']
        docstring = docopt(doc, argv)
        self.assertEqual(docstring['--version'], True)
        print docstring

    def testfor_suminput(self):
        argv = ['sum', '1', '2']
        docstring = docopt(doc, argv)
        self.assertEqual(docstring['sum'], True)
        self.assertEqual(docstring['<x>'], '1')
        self.assertEqual(docstring['<y>'], '2')
        print docstring

    def testfor_minusinput(self):
        argv = ['minus', '2', '1']
        docstring = docopt(doc, argv)
        self.assertEqual(docstring['minus'], True)
        self.assertEqual(docstring['<x>'], '2')
        self.assertEqual(docstring['<y>'], '1')
        print docstring


if __name__ == '__main__':
    unittest.main()

#do this stuff for the deployment cli
