class IPerception:
    '''
    The perception module needs to integrate several components:

    * agent physiology
    * agent coping style
    * prior emotional needs
    * any prior memory elements from previous 'cycles'

    '''
    EXPECTATION_COEFFICIENT = 1
    def getActionSet():
        '''
	Perception is coping mode-constrained, and this will limit the
	number/type of actions available.
        '''


'''
The senses.
'''

class ISmell:
    '''
    
    '''

class ITaste:
    '''

    '''

class IHearing:
    '''

    '''

class IVision:
    '''

    '''

class ITouch:
    '''

    '''

'''
Special cases.
'''

class INoise:
    '''
    A_t = f_d(A_t-1) + k * n_t

    * A sub t is the total activation and/or arousal/stress at time t
    * f sub d is the decay function
    * k is a constant representing susceptibility to noise
    * n sub t is the noise level at time t
    
    '''
