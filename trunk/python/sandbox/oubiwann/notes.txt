

import pydot
top = 'Standards'
n1 = 'Should not harm innocents'
n2 = 'Should fulfill commitments'
n12 = 'Bomb detonated with collatoral damage'
n11 = 'Mission ended without collatoral damage'
paths = [(top, n1), (top, n2), (n1, n11), (n1, n12)]
c1 = pydot.graph_from_edges(paths)
c1.write_jpeg('concern_tree1.jpg', prog='dot')

from graph.graph import Graph
G = {'y': {'s': 7, 'v': 6}, 'x': {'y': 2, 'u': 3, 'v': 9}, 's': {'x': 5, 'u': 10}, 'u': {'x': 2, 'v': 1}, 'v': {'y': 4}}
H = {'y': ('s', 'v'), 'x': ('y', 'u', 'v'), 's': ('x', 'u'), 'u': ['x', 'v'], 'v': 'y'} 
I = {
    'ontology': {'choice 1': 7, 'choice 2': 6},
    'choice 1': {'subchc 11': 1, 'subchc 12': 13},
    'choice 2': {'subchc 21': 4, 'subchc 22': 2},
}
G = Graph(G)
H = Graph(H)
I = Graph(I)
dot1 = I.fastGetDot()
dot1.write_jpeg('concern_tree1_dot.jpg', prog='dot')
dot1.write_jpeg('concern_tree1_neat.jpg', prog='neato')
dot2 = H.getDot()
dot2.write_jpeg('concern_tree2.jpg', prog='dot')

from adytum.math.graph import Graph
G = {
    'ontology': {'choice 1': 7, 'choice 2': 6, 'choice 3': 2, 'choice 4': 3},
    'choice 1': {'subchc 11': 1, 'subchc 12': 13},
    'choice 2': {'subchc 21': 4, 'subchc 22': 2},
    'choice 3': {'subchc 31': 10, 'subchc 32': 8, 'subchc 33': 5, 'subchc 22': 1},
    'choice 4': {'subchc 21': 4},
}
G = Graph(G)
dot1 = G.fastGetDot()
dot1.write_jpeg('concern_tree1_dot.jpg', prog='dot')

