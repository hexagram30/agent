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
WOLRD_INTERACTION = [i for i in 'EI']
WI = ATTITUDE = DIRECTION = WOLRD_INTERACTION
# Senesation/Perception
INTERNAL_VIEW = [i for i in 'NS']
IV = INTERNAL_VIEW
# Thinking/Feeling
INTERNAL_EXPERIENCE = [i for i in 'FT']
IE = DM = DECISION_MAKING = INTERNAL_EXPERIENCE
# Judgement/Perception
WORLD_VIEW = [i for i in 'JP']
WV = WORLD_VIEW

# thinkers
JG = ['ISTJ', 'ESTJ', 'ISFJ', 'ESFJ']
PG = ['ISTP', 'ESTP', 'ESFP', 'ISFP']
TG = ['ENTJ', 'INTJ', 'ENTP', 'INTP']
FG = ['ENFJ', 'INFJ', 'ENFP', 'INFP']

# Dominant Functions
EN = ['ENTP', 'ENFP']
ES = ['ESTP', 'ESFP']
EF = ['ESFJ', 'ENFJ']
ET = ['ESTJ', 'ENTJ']
IN = ['INTJ', 'INFJ']
IS = ['ISTJ', 'ISFJ']    
IF = ['ISFP', 'INFP']
IT = ['ISTP', 'INTP']

REFERENCE_PAIRS = [WI, IV, IE, WV]
RP = REFERENCE_PAIRS

POPULATION_MATRIX = array()

def getIndexForLetter(letter):
    '''
    This tells us which index of the reference pair array
    the input letter matches. This is how we standardize
    the ordering, so that the signed integers have
    meaning.
    '''
    return [ letter.upper() in pair for pair in RP ].index(True)

def getLetterForValue(letter_value, pair_index):
    '''
    '''
    values = RP[pair_index]
    keys = [ eval(x) for x in values ]
    return values[keys.index(letter_value)]
    
def getProperOrder(type_abbr):
    '''
    Order the input temperment type according to the order
    defined in the reference pairs.
    '''
    # setup a list with the proper length so that indices get
    # inserted into the proper place
    new = range(0,len(RP))
    # for every item we inert, it extends the list length by one.
    # the item that was at the index that was just inserted is now
    # at index + 1, so if we pop tht index, we're back the the 
    # proper length.
    [ (new.insert(getIndexForLetter(letter), letter), new.pop(getIndexForLetter(letter) + 1)) for letter in type_abbr ]
    return new
    
def getTempermentType(type_abbr):
    return [ eval(i.upper()) for i in getProperOrder(type_abbr) ]

def getArray(type_abbr):
    return array(getTempermentType(type_abbr))

def getTempermentString(type_list):
    return ''.join([ getLetterForValue(x[0], x[1]) for x in zip(type_list, range(0,len(type_list))) ])

def flipIndex(input_list, index):
    input_list.insert(index, input_list(index)*-1)
    input_list.pop(index+1)
    return input_list

def getMatchTypes(type_abbr):
    '''
    flip indices 0 (E/I) and then combine that with a separate
    flip of index 1 (N/S) and index 3 (J/P) 
    '''
    if type_abbr in T:
        #swap E/I and J/P
    
        # one one more, swap N/S
        pass
    elif type_abbr in F:
        #        
        pass
    from copy import copy
    match1 = getTempermentType(type_abbr)
    match1[0] *= -1             # flip E/I for all of them
    match2 = copy(match1)
    match3 = copy(match1)
    #match1[1] *= -1
    match2[2] *= -1
    match3[3] *= -1

    return (getTempermentString(match1), getTempermentString(match2), getTempermentString(match3))
    

class Temperment(object):
    def __init__(self):
        pass

    def getType(self, type_abbr):
        return array([ eval(i) for i in type_abbr ])
