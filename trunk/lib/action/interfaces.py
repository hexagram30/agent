class IAction:
    '''

    '''

class IUtilityPersonalityCOA:
    '''
    U(c) is the utility of the course of action.
    c is the course of action.
    P_x is personality aspect.
    E_x is the maximum emotional intensity x (or I_x) over all possible concern effects
        times the perceived probability of this outcome actually happening.

    U(c) = 
    P_surgence * (E_joy + E_satisfaction + E_relief + E_liking) +
    P_agreeableness * (E_happyfor + E_resentment - E_gloating - E_pity) - 
    P_conscientiousness * (E_distress + E_fearsconfirmed + E_disappointment + E_disliking) +
    P_conscientiousness * [(E_pride - E_shame) + (E_admiration - E_reproach)] - 
    P_openness * max(E) +
    P_emotionalstability * U(successor(c))
    '''

class IUtilitiyConsequnceCOA:
    '''
    u_j is the expected utility to each course of action at state j
    P_j is the probability at state j, based on the agents beliefs, that the goal will be achieved
    E_j is the sum across outcomes of utility times probability:

    E_j = COAScore_j = sum from j=1 to J of P_ij * u_j
    '''
