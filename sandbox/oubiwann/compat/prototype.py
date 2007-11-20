"""
This code is for exploring simple compatibility, using only math (i.e., with no
adjustments).
"""
from math import degrees
from numarray import *

# personalities
p1 = array([.5, .7, .4, .8, .3])
p2 = array([.3, .6, .6, .7, .3])
p3 = array([.8, .9, .7, .2, .6])
p4 = array([.8, .9, .7, .3, .6])

for p1, p2 in [(p1, p2), (p2, p3), (p3, p4), (p2, p4)]:
    theta = arccos(dot(p1, p2) / (sqrt(dot(p1, p1)) * sqrt(dot(p2, p2))))
    print "Separation: %s (%s)" % (theta, degrees(theta))
