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

# Dominant Functions
NDF = ['ENTP', 'ENFP', 'INTJ', 'INFJ']
SDF = ['ESTP', 'ESFP', 'ISTJ', 'ISFJ']
FDF = ['ESFJ', 'ENFJ', 'ISFP', 'INFP']
TDF = ['ESTJ', 'ENTJ', 'ISTP', 'INTP']
DOM_FUNC = {'N':NDF, 'S':SDF, 'F':FDF, 'T':TDF}

POPULATION_MATRIX = array()

def getIndexForLetter(letter):
    '''
    This tells us which index of the reference pair array
    the input letter matches. This is how we standardize
    the ordering, so that the signed integers have
    meaning.
    '''
    return [ letter.upper() in pair for pair in RP ].index(True)

def getValueForLetter(letter):
    '''
    This function doesn't care what grouping (index of RP) the letter is
    in, it just returns a 1 or -1, based on the constants defined above.
    '''
    return eval(letter)

def getLetterForValue(letter_value, pair_index):
    '''
    '''
    values = RP[pair_index]
    keys = [ eval(x) for x in values ]
    return values[keys.index(letter_value)]
    
def getProperOrder(type_abbr):
    '''
    Order the input temperament type according to the order
    defined in the reference pairs.
    '''
    # setup a list with the proper length so that indices get
    # inserted into the proper place
    new = range(0,len(RP))
    # for every item we inert, it extends the list length by one.
    # the item that was at the index that was just inserted is now
    # at index + 1, so if we pop that index, we're back the the 
    # proper length.
    [ (new.insert(getIndexForLetter(letter), letter), new.pop(getIndexForLetter(letter) + 1)) for letter in type_abbr ]
    return new
    
def getTemperamentList(type_abbr):
    '''
    This accepts a myers-briggs type (4 character string) as input,
    and returns a list of 1s and -1s representing the type components.
    '''
    return [ eval(i.upper()) for i in getProperOrder(type_abbr) ]

def getTemperamentArray(type_abbr):
    '''
    This is the same thing as getTemperamentList(), except that it
    returns the result as an numarray array type for linear algebra
    calculations, etc.
    '''
    return array(getTemperamentList(type_abbr))

def getTemperamentString(type_list):
    '''
    Process a list (or numeric array) and return the personality type
    as a standard 4 character myers-briggs string.
    '''
    return ''.join([ getLetterForValue(x[0], x[1]) for x in zip(type_list, range(0,len(type_list))) ])

def checkTemperament(type_abbr):
    '''
    This is a way of standardizing a string value for personality
    type. The called functions perform proper ordering and capitalization.
    '''
    try:
        return getTemperamentString(getTemperamentList(type_abbr))
    except:
        raise "PersonalityError: invalid myers-briggs string representation '%s'." % type_abbr

def getDominantFunction(type_list):
    '''
    Dominant functions are either in the T/F grouping or the S/P grouping.
    This function returns the letter abbreviation of the type (one of 'T', 'F',
    'S', or 'P').
    '''
    temperm = getTemperamentString(type_list)
    for func, temperm_list in DOM_FUNC.items():
        if temperm in temperm_list: return func

def getMatchTypes(type_list):
    '''
    Returns a tuple of possible good matches.

    The principles behind establishing "matches" or compatibilies between temperaments
    involve two things:
        1) temperaments that share dominant functions are well-suited for each other
        2) temperaments that have opposite "directions" (Introversion or Extroversion) 
        can well-suited for each other
        3) temperaments that have opposite ways of dealing with the world can be
        well-suited for each other.
        4) temperaments that share "information gathering" methods (Sensing or
        Intuition) can be well-suited for each other.

    This results in the following logic for possible good matches for a given 
    temperament:
        * switch the first index: if it was 'E', makd it 'I' and vice versa
        * find the dominant function, and keep that the same.
        * flip the last index: if it was 'J', make it 'P', and vice versa
        * there now remain two possibilities, provided be the two choices of
        the remaining index.
    '''
    match1 = type_list
    # if extrovert, make introvert, and vice versa
    match1[0] *= -1

    # flip world-dealing bit (last bit)
    match1[3] *= -1

    # setup the dominant function stuff, and flip non domin bit
    domin_func = getDominantFunction(type_list)
    domin_func_index = getIndexForLetter(domin_func)
    domin_func_value = getValueForLetter(domin_func)
    from copy import copy
    match2 = copy(match1)
    if domin_func_index == 2: match2[1] *= -1
    else: match2[2] *= -1

    return (getTemperamentString(match1), getTemperamentString(match2))

def getCompatibilityScale(person1, person2):
    '''
    This function attempts to scale between 0 and 1 the level of compatibility
    between two individuals, where 1 would be one of the two best matches and 0
    represent the oposite types. Decimal values between 0 and 1 attempt to 
    represent degree of compatibility. 
    '''
    pass

def getCompleteTemperamentStrings():
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
                    full_list.append(getTemperamentString([i,j,k,l]))
    return full_list

def getGeneticTemperament(parent1, parent2):
    '''
    The basic jist of this function is this: I wanted some way to produce semi-
    random "off-spring" that were the result of combinations of temperament types. 
    This is not meant to realistically model personality types of children based on
    the types of their parents. However, it does offer a nice way of auto-generating
    family trees/generations of temperaments.
    '''
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

