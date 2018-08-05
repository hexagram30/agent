"""
This code is for exploring simple compatibility, using only math (i.e., with no
adjustments).
"""
from math import degrees, pi
from numarray import array, arccos, dot, sqrt

from zope.interface import implements

import interfaces

class BasePersonality(object):

    implements(interfaces.IOCEAN)

    def __init__(self, scalars):
        self.original = list(scalars)
        self.array = array(scalars)
        self.setAttributes(scalars)

    def setAttributes(self, scalars):
        (self.openness, self.conscientiousness, self.surgency,
            self.agreeableness, self.emotionalstability) = scalars
        self.o, self.c, self.e, self.a, self.n = scalars
        self.extraversion = self.e
        self.neuroticism = self.n

    def getNorm(self):
        return sqrt(dot(self.array, self.array))

class Personality(BasePersonality):

    def getAngle(self, other):
        distance = dot(self.array, other.array)
        cosine = distance / (self.getNorm() * other.getNorm())
        angle = arccos(cosine)
        return angle

    def getCompatibility(self, other):
        maxAngle = pi / 2
        ratio = self.getAngle(other) / maxAngle
        return 100 - int(round(ratio*100))

def runTest():
    # personalities
    p1 = Personality([.5, .7, .4, .8, .3])
    p2 = Personality([.3, .6, .6, .7, .3])
    p3 = Personality([.8, .9, .7, .2, .6])
    p4 = Personality([.8, .9, .7, .3, .6])

    for p1, p2 in [(p1, p2), (p2, p3), (p3, p4), (p2, p4)]:
        theta = p1.getAngle(p2)
        compat = p1.getCompatibility(p2)
        print "Compatibility: %s%% (%s, %s)" % (compat, theta, degrees(theta))

if __name__ == '__main__':
    runTest()
