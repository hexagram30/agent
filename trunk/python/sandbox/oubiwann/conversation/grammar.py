from nltk.cfg import *

# Nonterminal is a simple class  that's used to let NLTK distinguish
# terminals from  nonterminals. Each Nonterminal is defined  by a
# symbol, which is represented by a  case-sensitive string. Typical
# symbols for  Nonterminals are "S"  (for sentence) and "NP" (for
# noun phrases).  To construct a Nonterminal, use the Nonterminal
# constructor: If you are defining many nonterminals at once, you can
# use the nonterminals() function.
S, VP, NP, PP = nonterminals('S, VP, NP, PP')
V, N, P, Name, Det = nonterminals('V, N, P, Name, Det')

class ToyGrammar(object):
    '''
    Grammer class.
    '''

    def __init__(self):

        # Context Free Grammar productions are represented with the CFGProduction
        # class. Each  CFGProduction specifies that a nonterminal  (the
        # left-hand side) can be expanded to  a sequence of terminals and
        # nonterminals (the  right-hand side).  CFGProductions are created
        # with the CFGProduction constructor, which  takes a nonterminal
        # left-hand side, and zero or more terminals  and nonterminals for
        # the right-hand side.  The right-hand side may contain any number
        # of elements.  In particular, for so-called epsilon  productions,
        # the right-hand side is empty. When parsing natural language, epsilon
        # productions are often used for  traces, which mark the position
        # from  which a constituant moved.
        self.productions = (
            CFGProduction(S, [NP, VP]),
            CFGProduction(NP, [Det, N]),
            CFGProduction(VP, [V, NP]),
            CFGProduction(VP, [V, NP, PP]),
            CFGProduction(NP, [Det, N, PP]),
            CFGProduction(PP, [P, NP]),
        )

        # Context free grammars are encoded by the CFG class. A  CFG consists
        # of a special  start nonterminal, and an ordered list  of productions.
        self.grammar = CFG(S, self.productions)

