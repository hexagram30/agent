class IEmotionalIntensity:
    '''
    Intensity of emotion. See the paper "How Emotion and Personality Effect the Utility of Alternate Decisions."
    '''
    def iHappyFor():
        '''
        '''
    def iGloating():
        '''
        '''
    def iResentment():
        '''
        '''
    def iPity():
        '''
        '''
    def iHope():
        '''
        '''
    def iFear():
        '''
        '''
    def iSatisfaction():
        '''
        '''
    def iFearsConfirmed():
        '''
        '''
    def iRelief():
        '''
        '''
    def iDisappointment():
        '''
        '''
    def iJoy():
        '''
        '''
    def iDistress():
        '''
        '''
    def iPride():
        '''
        '''
    def iShame():
        '''
        '''
    def iAdmiration():
        '''
        '''
    def iReproach():
        '''
        '''
    def iGratification():
        '''
        '''
    def iRemorse():
        '''
        '''
    def iAnger():
        '''
        '''
    def iGratitude():
        '''
        '''
    def iLiking():
        '''
        '''
    def iDisliking():
        '''
        '''

class IPhysioStressSubsystem:
    '''

    '''
    pass

class IEmotionalAppraisal:
    '''
    Ie(Sk) = intensity of emotion e due to the kth state of the world
    Je = the set of all agents relevant to emotion e. J1 is the set consisting only of the self. J2 is the set consisting of everyone but the self. J is the union of J1 and J2
    Cijkl = a list of paths through the ith ontology of agent j triggered to condition l (0=success or 1=failure) by stake k
    Wij(Cijkl) = the weighted importance of of the values of agent j that succeed and fail in one's ith concern set
    f1(rjk) = a function that captures the stringth of positive and negative relationships one has with the ja agents of objects that are effected or spared in state k
    f2(O,N) = a function that captures the temporal factors of the state and how to discount and merge one's emotions from the past, in the present and for the future.
    e = emtional pairs; there are 11 pairs of these, oppositely valenced (e.g. pride-shame, hope-fear)

    Equation:

    Ie(Sk) = Sum over each j belonging to Je of the Sum over each c belonging to Cijkl the product ( Wij(c) * f1(rjk) * f2(O,N) )

    Notes:

    agents have three types of concern tree about the world:
    1) goals for action
    2) standards that people should follow, and
    3) preferences for objects

    Sample usage:

    world_state = getWorldState()
    sum1 = 0
    for agent in set_of_agents:
        sets_of_concerns = getAgentConcerns(agent)
        sum2 = 0
        for concern_set in sets_of_concerns:
            w = getWieghtedImportanceOfSuccessFail(agent, concern_set)
            r = getRelationship(agent, world_state)
            f1 = getRelationshipStrength(r)
            o = XXX
            n = XXX
            f2 = XXX(o,n)
            sum2 += w * f1 * f2
        sum1 += sum2
            
            


    '''
    self_agent = property("")

    def getRelationship(agent_or_object, world_state):
        '''
        Obtain an object that represents the relationship between the 
        self_agent and the passed agent_or_object for the given state 
        of the world.

        Returns an object of type 'relationship'.
        '''
    def getRelationshipStrength(relationship):
        '''
        Calculate the strength of the passed relationship, positive 
        or negative.
        '''
    def getWeightedImportanceOfSuccessFail(agent, set_of_concerns):
        '''
        Calculate the weighted importance of agent's values that succeed
        or fail
        '''
    def getTemporalWorldStateFactors(XXX):
        '''
        '''
    def mergeOrDiscountTemportalEmotions(XXX):
        '''
        '''
    def getXXX(XXX):
        '''
        This method captures temportal factors of the state and captures
        how to discount and merge emotions from the past, in the present,
        and for the future.
        '''
    def sumConcernSets(agent, world_state, sets_of_concerns):
        '''
        This method loops over the list of ontology paths (sets_of_concerns).
         
        set_of_concerns is a set of sets.
        '''
    def getIntensity(emotion, world_state, set_of_agents, set_of_ontology_paths):
        '''
        Return the intensity of passed emotion based on the world state for
        a given set of agents and a given set of ontology paths.

        This method loops over the set_of_agents, calling sumOntologyPaths
        for each agent.
        '''

class IOCCModel:
    '''
    '''
    def evaluateSituation(XXX):
        '''
        '''
    def getReactionToEvent(XXX):
        '''
        To get a reaction to an event, an agent must have access to goals
        in relation to that event as well as 
        
        '''
class IOCCEventConsequence:
    '''
    '''

class IOCCAgentAction:
    '''
    '''

class IOCCObjectAspect:
    '''
    '''


