from adytum.aima import Object, Agent, XYEnvironment

# objects
class BarTop(Object): pass
class BarMop(Object): pass
class Glass(Object): pass
class Bottle(Object): pass

# agents
class Bartender(Agent): 
    '''
    The BT has the following actions:
        pickup bottle,
        put down bottle,
        replace the bottle
        fill the glass, 
        pick up mop,
        put down mop,
        wipe the bar, 
        talk to the patron, 
    The following goals:
        keep the glass full, 
        keep the bottle full, 
        keep the bartop clean, 
        keep the patron happy
    '''
   
class Patron(Agent): 
    '''
    The patron has the following actions:
        pick up glass,
        put down glass,
        drink from glass
        talk to bartender
    and the following goals:
        get drunk        
    '''

# environment
class Pub(XYEnvironment):

    def __init__(self, width=100, height=20):
        XYEnvironment.__init__(self, width, height)
        self.add_walls()

    object_classes = [BarTop, BarMop, Glass, Bottle, Bartender, Patron]

    
