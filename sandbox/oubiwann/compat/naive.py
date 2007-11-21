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
    """
    A function that embodies the rules for for the 'O' OCEAN component.
    """
    return getSameAttractsMultiplier(self, other) * medium

def getCMultiplier(self, other):
    """
    A function that embodies the rules for for the 'C' OCEAN component.
    """
    self = getMediumAttractMultiplier(self)
    other = getMediumAttractMultiplier(other)
    if .25 <= self <= .75 and .25 <= other <= .75:
        return getSameAttractsMultiplier(self, other) * mediumLow
    else:
        return getOppositeAttractsMultiplier(self, other) * mediumLow

def getEMultiplier(self, other):
    """
    A function that embodies the rules for for the 'E' OCEAN component.
    """
    return getSameAttractsMultiplier(self, other) * veryHigh

def getAMultiplier(self, other):
    """
    A function that embodies the rules for for the 'A' OCEAN component.
    """
    if self < 5:
        self = getLesserLowsMultiplier(self)
    if other < 5:
        other = getLesserLowsMultiplier(other)
    if self >= 5 and other >= 5:
        return getSameAttractsMultiplier(self, other) * low
    elif self < 5 and other < 5:
        return getSameRepelMultiplier(self, other) * low
    else:
        return getOppositeAttractsMultiplier(self, other) * low

def getNMultiplier(self, other):
    """
    A function that embodies the rules for for the 'N' OCEAN component.
    """
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
    """
    This is the inverse of the Gausian normal function.
    """
    return 1 - getNormal(x, coef, sigma, mu)

def getMediumAttractMultiplier(x):
    """
    For values of x approaching .5, this returns floats approaching 1.0. For
    values of x less than 0.25 and greater than 0.75, this returns floats
    approaching 0.0
    """
    return getNormal(x, .5, .2, .5)

def getEndsAttractMultiplier(x):
    """
    Useful for rules that emphasize the extreme ends (approaching zero and
    approaching one).
    """
    return getInverseNormal(x, .5, .2, .5)

def getSameAttractsMultiplier(self, other):
    """
    For rules where similar values need to attract, we need a large multiplier.
    Takng the difference gives small values, so subtracting from one produces
    values closer to one for more simmilar numbers.
    """
    return 1.0 - abs(self - other)
getOppositesRepelMultiplier = getSameAttractsMultiplier

def getOppositeAttractsMultiplier(self, other):
    """
    For rules where a disimilar values need to attract, the simple difference
    suffices.
    """
    return abs(self - other)
getSameRepelMultiplier = getOppositeAttractsMultiplier

def getLesserLowsMultiplier(x):
    """
    Useful when we want lower values to be even lower. Note that smaller values
    for multipliers will result in less contribution to the overall
    wieghtedness.
    """
    if x > .5:
        return x
    coef = x * pi / 4
    return coef * atan(pi * x)

def processRules(funcs, self, other):
    """
    Given a list of functions and two arrays representing the values for two
    different personalities, call the function corresponding to the personality
    attribute in each personality, passing the attributes.

    The returned array is an array of weighted values that will be used to
    modify the personality represented by "self" in relation to the personality
    represented by "other".
    """
    return array([func(*elems)
        for func, elems in zip(funcs, zip(self, other))])

def getSigns(data):
    """
    For the elements in self and other, determine the signs that need to be
    used in order to bring the corresponding elements of the arrays closer
    together.
    """
    signs = []
    for self, other in data:
        if self >= other:
            signs.append(-1)
        elif self < other:
            signs.append(1)
    return (array(signs), array(signs) * -1)

def getAdjustedCoefs(self, other, limiter=2):
    """
    Adjusted coefficents are needed in order to establish "true" compatiblity
    (as defined by arbitrary compatibility rules). There are several necessary
    bits of information needed in order to perform these calculations:
     * The distance between each corresponding element of the given vectors
     * The signs that represent whether addition or subtraction is needed in
       order for each element to approach the median distance
     * The functions that represent the rules that will be applied to each
       element
     * The processed coefficients that will be applied to the vectors
    """
    medianVector = abs(self- other)
    selfSigns, otherSigns = getSigns(zip(self, other))
    funcs = [getOMultiplier, getCMultiplier, getEMultiplier, getAMultiplier,
             getNMultiplier]
    selfRules = processRules(funcs, self, other)
    selfCoefs = selfRules * selfSigns * medianVector/limiter
    otherRules = processRules(funcs, other, self)
    otherCoefs = otherRules * otherSigns * medianVector/limiter
    return (selfCoefs, otherCoefs)

def getAdjustedPersonalities(self, other):
    """
    When personalities need to be checked for compatibility, rules need to be
    applied. These rules generate coefficients that can then be used to produce
    modified, temporary personalities whose angular separation can provide
    compatibility information based on the rules as applied to the two provided
    personalities.
    """
    selfCoefs, otherCoefs = getAdjustedCoefs(self.array, other.array)
    selfScalars = self.array + selfCoefs
    otherScalars = other.array + otherCoefs
    self = prototype.Personality(selfScalars)
    other = prototype.Personality(otherScalars)
    return (self, other)

class Personality(prototype.Personality):
    """
    A personality that provides a more sophisticated compatbility method than
    the simple vector math of it's parent class's method.
    """

    def __init__(self, *a, **k):
        prototype.Personality.__init__(self, *a, **k)

    def getCompatibility(self, other):
        adjusted = getAdjustedPersonalities(self, other)
        maxAngle = pi / 2 
        ratio = self.getAngle(other) / maxAngle
        orig = 100 - int(round(ratio*100))
        ratio = adjusted[0].getAngle(adjusted[1]) / maxAngle
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
