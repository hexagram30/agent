"""
This code takes compatibility beyond simple vector operations and introduces
some basic rules (taken from the OCEAN interface in personality.interfaces).

Rules:
 * openness - same attracts
   o .8 and .7 are a better match than .8 and .3
 * conscientiousness - extreme ends repel, medium levels attract
   o .8 and .7 are a better match than .8 and .3
 * surgency - same attracts
   o .8 and .7 are a better match than .8 and .3
   o .2 and .3 are a better match than .8 and .3
 * agreeableness - opposites attract, same highs attract, same lows repel
   o .1 and .9 attract
   o .8 and .9 attract
   o .1 and .2 repel
 * emotionalstability - same attracts
   o .8 and .7 are a better match than .8 and .3

Same attracts: the multiplier is the scalar difference subtracted from 1
Opposite attracts: the multiplier is the scalar difference
Medium levels contributing more than extreme ends: use normal curve

"""
from math import pi, exp, degrees, atan, sqrt

from numarray import array

import prototype

veryHigh = 5./5.
high = 4./5.
medium = 3./5.
mediumLow = 2./5.
low = 1./5.

def getOMultiplier(self, other):
    return getSameAttractsMultiplier(self, other) * medium

def getCMultiplier(self, other):
    self = getMediumAttractMultiplier(self)
    other = getMediumAttractMultiplier(other)
    if .25 <= self <= .75 and .25 <= other <= .75:
        return getSameAttractsMultiplier(self, other) * mediumLow
    else:
        return getOppositeAttractsMultiplier(self, other) * mediumLow

def getEMultiplier(self, other):
    return getSameAttractsMultiplier(self, other) * veryHigh

def getAMultiplier(self, other):
    if self >= 5 and other >= 5:
        return getSameAttractsMultiplier(self, other) * low
    elif self < 5 and other < 5:
        return getSameRepelMultiplier(self, other) * low
    else:
        return getOppositeAttractsMultiplier(self, other) * low

def getNMultiplier(self, other):
    return getSameAttractsMultiplier(self, other) * medium

def getNormal(x, coef=1, sigma=1, mu=1):
    """
    This is the equation for the probability density function of a normal
    distribution.
    """
    exponentValue = -(x-mu)**2 / 2*sigma**2
    coef = coef * 1 / (sigma * sqrt(2*pi))
    return coef * exp(exponentValue)

def getInverseNormal(x, coef=1, sigma=1, mu=1):
    return 1 - getNormal(x, coef, sigma, mu)

def getMediumAttractMultiplier(x):
    """
    For values of x approaching .5, this returns floats approaching 1.0. For
    values of x less than 0.25 and greater than 0.75, this returns floats
    approaching 0.0
    """
    return getNormal(x, .5, .2, .5)

def getEndsAttractMultiplier(x):
    return getInverseNormal(x, .5, .2, .5)

def getSameAttractsMultiplier(self, other):
    return 1.0 - abs(self - other)
getOppositesRepelMultiplier = getSameAttractsMultiplier

def getOppositeAttractsMultiplier(self, other):
    return abs(self - other)
getSameRepelMultiplier = getOppositeAttractsMultiplier

def getLowsRepelMultiplier(x):
    if x > .5:
        return x
    coef = x * pi / 4
    return coef * atan(pi * x)

def processRules(funcs, self, other):
    return array([func(*elems)
        for func, elems in zip(funcs, zip(self, other))])

def getSigns(data):
    signs = []
    for self, other, median in data:
        if self >= other:
            signs.append(-1)
        elif self < other:
            signs.append(1)
    return (array(signs), array(signs) * -1)

def getAdjustedCoefs(self, other):
    medianVector = abs(self- other)
    selfSigns, otherSigns = getSigns(zip(self, other, medianVector))
    print "Median vector: %s" % medianVector
    funcs = [getOMultiplier, getCMultiplier, getEMultiplier, getAMultiplier,
             getNMultiplier]
    selfCoefs = processRules(funcs, self, other) * selfSigns * medianVector/2
    otherCoefs = processRules(funcs, other, self) * otherSigns * medianVector/2
    return (selfCoefs, otherCoefs)

def getAdjustedPersonalities(self, other):
    selfCoefs, otherCoefs = getAdjustedCoefs(self.array, other.array)
    print "Coefs: ", selfCoefs, otherCoefs
    selfScalars = self.array + selfCoefs
    otherScalars = other.array + otherCoefs
    print "New scalars: ", selfScalars, otherScalars
    self = prototype.Personality(selfScalars)
    other = prototype.Personality(otherScalars)
    return (self, other)

class Personality(prototype.Personality):

    def __init__(self, *a, **k):
        prototype.Personality.__init__(self, *a, **k)

    def getCompatibility(self, other):
        print self.array, other.array
        adjusted = getAdjustedPersonalities(self, other)
        maxAngle = pi / 2 
        ratio = self.getAngle(other) / maxAngle
        orig = 100 - int(round(ratio*100))
        print "Original compatibility: %s%%" % orig
        ratio = adjusted[0].getAngle(adjusted[1]) / maxAngle
        return 100 - int(round(ratio*100))

# personalities
p1 = Personality([.5, .7, .4, .8, .3])
p2 = Personality([.3, .6, .6, .7, .3])
p3 = Personality([.8, .9, .7, .2, .6])
p4 = Personality([.8, .9, .7, .3, .6])
    
for p1, p2 in [(p1, p2), (p2, p3), (p3, p4), (p2, p4)]:
    theta = p1.getAngle(p2)
    compat = p1.getCompatibility(p2)
    print "Compatibility: %s%% (%s, %s)" % (compat, theta, degrees(theta))
