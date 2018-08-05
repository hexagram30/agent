from nltk.cfg import *
from nltk.tokenizer import WhitespaceTokenizer
from nltk.parser import RecursiveDescentParser

# build a grammar
S, VP, NP, PP = nonterminals('S, VP, NP, PP')
V, N, P, Name, Det = nonterminals('V, N, P, Name, Det')

productions = (
    CFGProduction(S, [NP, VP]),
    CFGProduction(NP, [Det, N]),
    CFGProduction(VP, [V, NP]),
    CFGProduction(VP, [V, NP, PP]),
    CFGProduction(NP, [Det, N, PP]),
    CFGProduction(PP, [P, NP]),

    CFGProduction(NP, ['I']),   CFGProduction(Det, ['the']),
    CFGProduction(Det, ['a']),  CFGProduction(N, ['man']),
    CFGProduction(V, ['saw']),  CFGProduction(P, ['in']),
    CFGProduction(P, ['with']), CFGProduction(N, ['park']),
    CFGProduction(N, ['dog']),   CFGProduction(N, ['telescope'])
)
grammar = CFG(S, productions)

# Tokenize a simple sentence 
sentence = 'I saw a man in the park'
sent = Token(TEXT=sentence)
print sent
print type(sent)
WhitespaceTokenizer().tokenize(sent)
print sent
        
# Build a parser 
parser = RecursiveDescentParser(grammar)
print dir(parser)
print parser.__dict__
for p in parser.get_parse_list(sent):
    print p

print '\n\n\n'

from parser import Parser
p = Parser()
p.setSentence('I move slowly south')
print p
print p.sentence
print p._sentence


import parser
token = parser.Token('I move slowly towards the West, sneaking up on the Grue with my sword drawn.')
tagger = parser.Tagger(texts=40)
tagger.tagger.tag(token.text_token)
token.text_token
sent = token.getTaggedString()

from nltk.tokenreader.tagged import *
from nltk.parser.chunk import *

reader = TaggedTokenReader(SUBTOKENS='WORDS')
sent_token = reader.read_token(sent)
chunk_rule = ChunkRule('<NN.*|DT|JJ>+','Chunk sequences of NN, JJ, and DT')
split_rule = SplitRule('<NN>', '<DT>','Split NN followed by DT')
chunkparser = RegexpChunkParser([chunk_rule, split_rule],
    chunk_node='NP', top_node='S', SUBTOKENS='WORDS')
chunkparser.parse(sent_token)
print sent_token['TREE']


