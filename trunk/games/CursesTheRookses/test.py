import unittest
import doctest
import sys
sys.path.append('./lib')

modules = [
    #'imagination.test', # they don't use doc tests...
    'games.rookcurses.map',
]

suite = unittest.TestSuite()
for modname in modules:
    mod = __import__(modname)
    components = modname.split('.')
    #print mod, components, components[1:]
    if len(components) == 1:
        suite.addTest(doctest.DocTestSuite(mod))
    else:
        for comp in components[1:]:
            try:
                mod = getattr(mod, comp)
                #print "Adding mod '%s'..." % mod
                suite.addTest(doctest.DocTestSuite(mod))
            except ValueError:
                pass
runner = unittest.TextTestRunner()
runner.run(suite)        
