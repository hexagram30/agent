from protocols import Interface
'''
General body interfaces. Body as in car body, robot body, human body.
'''

class IBody(Interface):
    '''
    
    '''


'''
Human aspects.
'''

# Initial input and advice supplied by Dr. Douglass McGreggor, D.O.

class IHeartRate(Interface):
    '''
    The heart beat causes a pressure wave through the arteries; the perception
    of this is termed the "pulse" and is a signifier of the heart rate or heart
    beat. We are interested in changes here, so rate it a better word choice.
    '''

class IBloodPressure(Interface):
    '''
    This has a very subtle effect and should not contribute very much. Perhaps
    this should be a long term effect. This would only have an immediate and
    noticable effect under extreme change. Shock affects blood pressure.
    '''

class IFuel(Interface):
    '''
    This should address such things as quantity and quality of food supply,
    regularity.
    '''

class IRespiration(Interface):
    '''
    Supplies the fire to burn the fuel, as it were.
    '''

class IPerspiration(Interface):
    '''
    This may not be a good one. It's more an indication or effect, than a
    cause... but that could be argued both ways.
    '''

class IBodyTemperature(Interface):
    '''
    Has a significant and powerful effect of an agent's state of being. It has a
    very narrow range for optimal conditions.
    '''

class ISleep(Interface):
    '''
    Sleep is a restorative function... one could also view sleep from the
    perspective of storage, accumlation, quantity, etc., and thus as a micro
    economy like fuel.
    '''

class IExertion(Interface):
    '''
    Pronounced (quantifiable), physical expenditure of energy.
    '''

