from protocols import Interface
'''
General body interfaces. Body as in car body, robot body, human body.
'''

class IBody(Interface):
    '''
    
    '''
    def getFuelLevel():
        '''
        This should address such things as quantity and quality of energy supply,
        regularity.
        '''

    def getBodyTemperature():
        '''
        Has a significant and powerful effect of an agent's state of being. It has a
        very narrow range for optimal conditions.
        '''

    def getDamageLevel():
        '''

        '''

'''
Specifically human aspects.
'''

# Initial input and advice supplied by Dr. Douglass McGreggor, D.O.
class IPhysiology(Component):

    def getHeartRate():
        '''
        The heart beat causes a pressure wave through the arteries; the perception
        of this is termed the "pulse" and is a signifier of the heart rate or heart
        beat. We are interested in changes here, so rate it a better word choice.
        '''

    def getBloodPressure():
        '''
        This has a very subtle effect and should not contribute very much. Perhaps
        this should be a long term effect. This would only have an immediate and
        noticable effect under extreme change. Shock affects blood pressure.
        '''

    def getRespiration():
        '''
        Supplies the fire to burn the fuel, as it were.
        '''

    def getPerspiration():
        '''
        This may not be a good one. It's more an indication or effect, than a
        cause... but that could be argued both ways.
        '''

    def getSleep():
        '''
        Sleep is a restorative function... one could also view sleep from the
        perspective of storage, accumlation, quantity, etc., and thus as a micro
        economy like fuel.
        '''

    def getExertion():
        '''
        Pronounced (quantifiable), physical expenditure of energy.
        '''

