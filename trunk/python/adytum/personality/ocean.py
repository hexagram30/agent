import protocols 
from peak.binding.components import Component
from interfaces import IOCEAN

# Constants
O = 'Openness to Experience'
C = 'Conscientiousness'
E = 'Surgency'
A = 'Agreeableness'
N1 = 'Emotional Stability'
N2 = 'Neuroticism'
FACTORS = [O,C,E,A,N1,N2]
FACETS = {
    O:['Imagination', 'Artistic Interests', 'Emotions', 'Adventurousness', 'Intellect', 'Liberalism'],
    C:['Resourcefulness', 'Orderliness', 'Sense of Duty', 'Achievement Striving', 'Self-Discipline', 'Cautiousness'],
    E:['Friendliness', 'Gregariousness', 'Assertiveness', 'Activity Level', 'Excitement Seeking', 'Cheerfulness'],
    A:['Trust', 'Morality', 'Altruism', 'Co-operation', 'Modesty', 'Sympathy'],
    N1:['Ease/Positiveness', 'Gratitude', 'Joy', 'Self-Confidence', 'Moderation', 'Security/Stability'],
    N2:['Anxiety/Worrying', 'Anger', 'Depression', 'Low Self-Esteem/Self-Consciousness', 'Immoderation', 'Vulnerability'],
}

class OCEAN(Component):
    '''
    For full documentation, see interfaces.IOCEAN. Example usage and doctest:
    >>> from ocean import OCEAN
    >>> me = (0.8666666666666667, 0.58333333333333337, 0.78333333333333333, 0.65000000000000002, 0.77499999999999991)
    >>> o = OCEAN(me)
    >>> test = (0.5,0.5,0.5,0.5,0.5)
    >>> o.setFactors(test)
    >>> o.getFactors()
    (0.5, 0.5, 0.5, 0.5, 0.5)
    >>> o.setFactors(me)
    >>> o.getFactors()
    (0.8666666666666667, 0.58333333333333337, 0.78333333333333333, 0.65000000000000002, 0.77499999999999991)
    >>> o.mergeFactors(test, weight=0)
    >>> o.getFactors()
    (0.8666666666666667, 0.58333333333333337, 0.78333333333333333, 0.65000000000000002, 0.77499999999999991)
    >>> o.mergeFactors(test, weight=1)
    >>> o.getFactors()
    (0.68333333333333335, 0.54166666666666674, 0.64166666666666661, 0.57499999999999996, 0.63749999999999996)
    >>> o.mergeFactors(test, weight=2)
    >>> o.getFactors()
    (0.56111111111111112, 0.51388888888888895, 0.54722222222222217, 0.52500000000000002, 0.54583333333333328)
    >>> o.mergeFactors(test, weight=10)
    >>> o.getFactors()
    (0.50555555555555554, 0.5012626262626263, 0.50429292929292935, 0.50227272727272732, 0.50416666666666665)
    '''
    protocols.advise(instancesProvide=[IOCEAN])

    def __init__(self, default=(0.5,0.5,0.5,0.5,0.5)):
        self.setFactors(default)

    def setFactors(self, factors):

        self.openness = factors[0]
        self.conscientiousness = factors[1]
        self.surgency = factors[2]
        self.agreeableness = factors[3]
        self.emotionalstability = factors[4]

    def getFactors(self):
        return (self.openness, self.conscientiousness, self.surgency,
            self.agreeableness, self.emotionalstability)

    def mergeFactors(self, factors, weight=1):
        old_factors = self.getFactors()
        to_merge = zip(old_factors, factors)
        to_merge = [ (x[0] + x[1]*weight)/(1+weight) for x in to_merge ]
        self.setFactors(to_merge)
        

QUIZ_SCALE = 10
def question(facet):
    question_template = '''On a scale from 1 to %s, how would you rate youself regarding '%s'? ''' % (QUIZ_SCALE, facet)
    result = raw_input(question_template)
    try:
        result = int(result)
        if result > QUIZ_SCALE: raise
        if result < 1: raise
    except:
        print "Error: could not cast your input as an integer between 1 and %s." % QUIZ_SCALE
        print "Please try again..."
        result = question(facet)
    return int(result)
    
def quiz():
    results = {O:0, C:0, E:0, A:0, N1:0, N2:0}
    for factor, facets in FACETS.items():
        for facet in facets:
            results[factor] += question(facet)
        facet_count = len(FACETS[factor])
        results[factor] = results[factor] / float(facet_count * QUIZ_SCALE)
        if factor == N2:
            results[factor] = 1 - results[factor]
    results[N1] = (results[N1] + results[N2]) / 2
    tuple_result = [ results[factor]  for factor in FACTORS]
    tuple_result.pop(-1)
    FACTORS.pop(-1)
    tuple_result = tuple(tuple_result)
    # combine the two aspects of N 
    
    print 'Your results:'
    print '\t%s' % str(tuple_result)
    for factor in FACTORS:
        print '\t%s: %f' % (factor, results[factor])
    
def _test():
    import doctest, ocean
    return doctest.testmod(ocean)

if __name__ == '__main__':
    _test()
    check = raw_input("\nWould you like to take the quiz? (Y/N) ")
    if check in ['Y','y','1','yes','Yes','YES']:
        quiz()
    else:
        print "Exiting..."
