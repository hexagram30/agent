#from nltk.token import Token
from nltk import tokenizer
from nltk.tagger import *
from nltk.parser import RecursiveDescentParser as Parser
from nltk.tokenreader.tagged import ChunkedTaggedTokenReader

from grammar import ToyGrammar as Grammar

class Error(Exception):
    pass

class TokenError(Error):
    pass

class TaggerError(Error):
    pass

class ParserError(Error):
    pass

class Token(object):
    '''
    Token class for the parsers.

    Example usage:
    >>> import parser
    >>> token = parser.Token('I move slowly towards the West')
    >>> token.text_token
    <[<I>, <move>, <slowly>, <towards>, <the>, <West>]>
    >>> token.isTagged()
    False
    '''
    def __init__(self, text):
        self.text = text
        self.text_token = None
        self.tokenize()
    
    def tokenize(self):
        from nltk import tokenizer
        token = tokenizer.Token(TEXT=self.text)
        tokenizer.WhitespaceTokenizer().tokenize(token)
        self.text_token = token

    def isTagged(self):
        if not self.text_token['SUBTOKENS']:
            return False
        if 'TAG' in self.text_token['SUBTOKENS'][0].properties():
            return True
        return False

    def getTaggedString(self):
        if self.isTagged():
            sub = self.text_token['SUBTOKENS']
            return ' '.join([ '%s/%s' % (x['TEXT'],x['TAG'].upper()) for x in sub ])

class Tagger(object):
    '''
    Tagger class for use by ChunkedParser.

    Example usage:
    >>> import parser
    >>> token = parser.Token('I move slowly towards the West')
    >>> tagger = parser.Tagger(texts=40)
    >>> tagger.tagger.tag(token.text_token)
    >>> token.text_token
    <[<I/ppss>, <move/vb>, <slowly/rb>, <towards/in>, <the/at>, <West/nr-tl>]>
    >>> token.isTagged()
    True
    >>> token.getTaggedString()
    'I/PPSS move/VB slowly/RB towards/IN the/AT West/NR-TL'
    '''
    def __init__(self, texts=10):
        self.tagger = None
        self.taggers_trained = False
        self.train_tokens = []
        nth_tagger = NthOrderTagger(1, SUBTOKENS='WORDS')
        uni_tagger = UnigramTagger(SUBTOKENS='WORDS')
        reg_tagger = RegexpTagger([(r'^[0-9]+(.[0-9]+)?$', 'cd'), (r'.*', 'nn')], 
            SUBTOKENS='WORDS')
        self.tagger_list = [nth_tagger, uni_tagger, reg_tagger]
        self.buildTrainTokens(texts)
        self.trainTaggers()
        self.buildTagger()

    def buildTrainTokens(self, texts=10):
        '''
        Tokenize texts from the Brown Corpus.
        '''
        from nltk.corpus import brown

        train_tokens = []
        for item in brown.items()[:texts]:
            train_tokens.append(brown.read(item))
        self.train_tokens = train_tokens

    def trainTaggers(self):
        if not self.train_tokens:
            raise TaggerError, 'cannot train taggers without tokens'
        for tok in self.train_tokens:
            [ tagger.train(tok) for tagger in self.tagger_list 
                if 'train' in dir(tagger) ]
        self.taggers_trained = True

    def buildTagger(self):
        if not self.tagger_list:
            raise TaggerError, 'cannot build Backoff without a list of taggers'
        if not self.taggers_trained:
            raise TaggerError, 'cannot build Backoff without trained taggers'
        self.tagger = BackoffTagger(self.tagger_list)

class Chunker(object):
    '''
    A chunk parser class.
    '''
    def __init__(self, sent_string):
        from nltk.tokenreader.tagged import TaggedTokenReader
        reader = TaggedTokenReader(SUBTOKENS='WORDS')
        sent_token = reader.read_token(sent)
        self.reader = reader
        self.sent_token = sent_token
        self.rule_list = []
        self.chunkparser = None
        self.is_parsed = False

    def setupRules(self):
        # rule 1
        # rule 2
        # rule 3
        # rule 4
        self.chunkparser = RegexpChunkParser(self.rule_list)

    def parse(self):
        self.chunkparser.parse(self.sent_token)

class ChunkParser(object):
    '''
    A Parsing wrapper class.
    '''
    def __init__(self, string=''):
        token = Token()
        tagger = Tagger()
        chunker = Chunker()

    def updateString(self):
        # update token
        # update tagger
        # update chunker
        pass

class Parser(object):
    '''
    Parser class.

    >>> p = Parser()
    >>> print type(p)
    <class 'parser.Parser'>

    # test exceptions
    >>> p.tokenize()
    Traceback (most recent call last):
        raise ParserError, 'cannot tokenize empty sentence'
    ParserError: cannot tokenize empty sentence
    >>> 

    >>> p.getParseList()
    Traceback (most recent call last):
        raise ParserError, 'cannot parse empty sentence'
    ParserError: cannot parse empty sentence
    >>> 


    >>> p.setSentence('I move quickly East')
    '''
    def __init__(self, sentence=''):

        grammar = Grammar()
        self.grammar = grammar.grammar
        self.parser = None
        if sentence:
            self.setSentence(sentence)
        else:
            self.sentence = sentence

    def tokenize(self):
        
        from copy import copy
        if not self.sentence:
            raise ParserError, 'cannot tokenize empty sentence'

        _sentence = tokenizer.Token(TEXT=self.sentence)
        tokenizer.WhitespaceTokenizer().tokenize(_sentence)
        self._sentence = _sentence

    def setParser(self):
        
        self.parser = Parser(self.grammar)

    def getParser(self):

        if not self.parser:
            self.setParser()

        return self.parser

    # XXX getParseList is broken right now...
    def getParseList(self):

        if not self.sentence:
            raise ParserError, 'cannot parse empty sentence'

        if not self.parser:
            self.setParser()

        return self.parser.get_parser_list(self._sentence)

    def setSentence(self, sentence=''):

        self.sentence = sentence
        self.tokenize()
        

def _test():
    import doctest, parser
    return doctest.testmod(parser)

if __name__ == '__main__':
    _test()


