import protocols
from peak.binding.components import Component
from interfaces import IMyersBriggs
from numarray import array

# Setup personality components
E = 1
I = -1
N = 1
S = -1
F = 1
T = -1
J = 1
P = -1

# Introvery/Extrovert
WOLRD_INTERACTION = ['E', 'I']
WI = ATTITUDE = DIRECTION = WOLRD_INTERACTION
# Senesation/Perception
INTERNAL_VIEW = ['N', 'S']
IV = INTERNAL_VIEW
# Thinking/Feeling
INTERNAL_EXPERIENCE = ['F', 'T']
IE = DM = DECISION_MAKING = INTERNAL_EXPERIENCE
# Judgement/Perception
WORLD_VIEW = ['J', 'P']
WV = WORLD_VIEW

REFERENCE_PAIRS = [WI, IV, IE, WV]
RP = REFERENCE_PAIRS

# guardians
JG = ['ISTJ', 'ESTJ', 'ISFJ', 'ESFJ']
# artisans
PG = ['ISTP', 'ESTP', 'ESFP', 'ISFP']
# rationals
TG = ['ENTJ', 'INTJ', 'ENTP', 'INTP']
# idealists
FG = ['ENFJ', 'INFJ', 'ENFP', 'INFP']
TYPE_GROUPS = {'JG':JG,'PG':PG,'TG':TG,'FG':FG}

# Dominant Functions
NDF = ['ENTP', 'ENFP', 'INTJ', 'INFJ']
SDF = ['ESTP', 'ESFP', 'ISTJ', 'ISFJ']
FDF = ['ESFJ', 'ENFJ', 'ISFP', 'INFP']
TDF = ['ESTJ', 'ENTJ', 'ISTP', 'INTP']
DOM_FUNC = {'N':NDF, 'S':SDF, 'F':FDF, 'T':TDF}

POPULATION_MATRIX = array()

class MyersBriggs(Component):
    '''
    >>> from myersbriggs import MyersBriggs
    >>> mb = MyersBriggs()
    >>> mb.getIndexForLetter('I')
    0
    >>> mb.getIndexForLetter('E')
    0
    >>> mb.getIndexForLetter('J')
    3
    >>> mb.getIndexForLetter('T')
    2
    >>> mb.getIndexForLetter('N')
    1
    >>> mb.getValueForLetter('E')
    1
    >>> mb.getValueForLetter('I')
    -1
    >>> mb.getLetterForValue(-1, 3)
    'P'
    >>> mb.getLetterForValue(1, 0)
    'E'
    >>> mb.getProperOrder('pint')
    ['i', 'n', 't', 'p']
    >>> mb.getTemperamentList('intp')
    [-1, 1, -1, -1]
    >>> mb.getTemperamentString([-1, 1, -1, -1])
    'INTP'
    >>> mb.checkTemperament('pint') 
    'INTP'
    >>> mb.getDominantFunction([-1, 1, -1, -1])
    'T'
    >>> mb.getMatchTypes([-1, 1, -1, -1])
    ('ENTJ', 'ESTJ')
    >>> mb.getCompleteTemperamentStrings()
    ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']
    ''' 

    protocols.advise(instancesProvide=[IMyersBriggs])

    def __init__(self, type_abbr=None):
        self.type_abbr = type_abbr
        if type_abbr:
            self.type_abbr = self.checkTemperament(type_abbr)
            self.type_list = self.getTemperamentList(type_abbr)

    def getIndexForLetter(self, letter):
        return [ letter.upper() in pair for pair in RP ].index(True)

    def getValueForLetter(self, letter):
        return eval(letter)

    def getLetterForValue(self, letter_value, pair_index):
        values = RP[pair_index]
        keys = [ eval(x) for x in values ]
        return values[keys.index(letter_value)]
        
    def getProperOrder(self, type_abbr):
        # setup a list with the proper length so that indices get
        # inserted into the proper place
        new = range(0,len(RP))
        # for every item we inert, it extends the list length by one.
        # the item that was at the index that was just inserted is now
        # at index + 1, so if we pop that index, we're back the the 
        # proper length.
        [ (new.insert(self.getIndexForLetter(letter), letter), 
            new.pop(self.getIndexForLetter(letter) + 1)) for letter in type_abbr ]
        return new
        
    def getTemperamentList(self, type_abbr):
        return [ eval(i.upper()) for i in self.getProperOrder(type_abbr) ]

    def getTemperamentArray(self, type_abbr):
        return array(self.getTemperamentList(type_abbr))

    def getTemperamentString(self, type_list):
        return ''.join([ self.getLetterForValue(x[0], x[1]) for x 
            in zip(type_list, range(0,len(type_list))) ])

    def checkTemperament(self, type_abbr):
        try:
            return self.getTemperamentString(self.getTemperamentList(type_abbr))
        except:
            raise "PersonalityError: invalid myers-briggs string representation '%s'." % type_abbr

    def getDominantFunction(self, type_list):
        temperm = self.getTemperamentString(type_list)
        for func, temperm_list in DOM_FUNC.items():
            if temperm in temperm_list: return func

    def getMatchTypes(self, type_list):
        match1 = type_list
        # if extrovert, make introvert, and vice versa
        match1[0] *= -1

        # flip world-dealing bit (last bit)
        match1[3] *= -1

        # setup the dominant function stuff, and flip non domin bit
        domin_func = self.getDominantFunction(type_list)
        domin_func_index = self.getIndexForLetter(domin_func)
        domin_func_value = self.getValueForLetter(domin_func)
        from copy import copy
        match2 = copy(match1)
        if domin_func_index == 2: match2[1] *= -1
        else: match2[2] *= -1

        return (self.getTemperamentString(match1), 
            self.getTemperamentString(match2))

    def getCompatibilityScale(self, person1, person2):
        pass

    def getCompleteTemperamentStrings(self):
        # XXX This seems hackish to me, or at the least, inellegant. There must be
        # a nice clever way to do this that involve list comprehensions, or 
        # iterators, or generators...
        #
        # this is basically just binary math, whether you are using 0/1, -1/1, E/I,
        # etc., it's all the same thing. An elegant solution will take advantage of
        # the fact that this is binary math...
        full_list = []
        for i in [1,-1]:
            for j in [1,-1]:
                for k in [1,-1]:
                    for l in [1,-1]:
                        full_list.append(self.getTemperamentString([i,j,k,l]))
        return full_list

    def getGeneticTemperament(self, parent1, parent2):
        # generate a random "mask" list, composed of true and false booleans
        # e.g. : [False, True, False, True]
        from random import random
        from math import ceil
        mask = [ bool(int(ceil(random() * 2)) % 2) for x in range(0,4) ]
        # pair off the ith element of each list (mask, parent1 and parent2) in a new list
        combo = zip(mask, parent1, parent2)

        # for every True in each element of the combo list, take the corresponding element 
        # from parent1, and for every False, take the corresponding element from parent2,
        # thus giving a new temperament that is the result of the combination of two parents.
        def checkit(part):
            if part[0]: return part[1]
            return part[2]

        return [ checkit(x) for x in combo ]

    def getOCEANMap(self):
        import numarray 
        from ocean import OCEAN
        oc = OCEAN()
        total_list = []

        E_OCEAN = (0.5, 0.5, 0.8, 0.5, 0.5)
        I_OCEAN = (0.5, 0.5, 0.2, 0.5, 0.5)
        N_OCEAN = (0.5, 0.4, 0.5, 0.4, 0.5)
        S_OCEAN = (0.5, 0.6, 0.5, 0.6, 0.5)
        F_OCEAN = (0.8, 0.5, 0.5, 0.5, 0.5)
        T_OCEAN = (0.8, 0.5, 0.5, 0.5, 0.5)
        J_OCEAN = (0.3, 0.6, 0.5, 0.5, 0.5)
        P_OCEAN = (0.6, 0.3, 0.5, 0.5, 0.5)

        letter_list = self.getProperOrder(self.type_abbr)
        type_ocean = [ eval('%s_OCEAN' % x) for x in letter_list ]

        weight = 3
        for i in range(0,weight):
            total_list.extend(total_list)

        # guardians
        JG_OCEAN = (0.5, 0.7, 0.5, 0.7, 0.4)
        # artisans
        PG_OCEAN = (0.7, 0.5, 0.6, 0.5, 0.4)
        # rationals
        TG_OCEAN = (0.7, 0.6, 0.6, 0.4, 0.6)
        # idealists
        FG_OCEAN = (0.7, 0.6, 0.5, 0.4, 0.7)

        group_letter = [ x for x in TYPE_GROUPS.keys() if self.type_abbr in TYPE_GROUPS[x] ][0]
        total_list.append(eval('%s_OCEAN' % group_letter))

        # Dominant Functions
        NDF_OCEAN = (0.5, 0.4, 0.5, 0.4, 0.5)
        SDF_OCEAN = (0.5, 0.6, 0.5, 0.6, 0.5)
        FDF_OCEAN = (0.8, 0.5, 0.5, 0.5, 0.5)
        TDF_OCEAN = (0.8, 0.5, 0.5, 0.5, 0.5)

        dom_letter = [ x for x in DOM_FUNC.keys() if self.type_abbr in DOM_FUNC[x]][0]
        total_list.append(eval('%sDF_OCEAN' % dom_letter))

        return tuple([ x/len(total_list) for x in numarray.sum(total_list) ])

def _test():

    import doctest, myersbriggs
    return doctest.testmod(myersbriggs)

if __name__ == '__main__':
    _test()
