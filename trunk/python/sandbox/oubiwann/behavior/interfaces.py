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
        Calculates the strength of the passed relationship, positive 
        or negative.
        '''
    def getIntensity(emotion, world_state, set_of_agents, set_of_ontology_paths):
        '''

        '''
