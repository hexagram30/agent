def test_tagging():
    '''
    >>> from nltk.tokenizer import *
    >>> text_token = Token(TEXT="John saw 3 polar bears .")
    >>> WhitespaceTokenizer().tokenize(text_token)
    >>> #WhitespaceTokenizer(SUBTOKENS='WORDS').tokenize(text_token)
    >>> print text_token
    <[<John>, <saw>, <3>, <polar>, <bears>, <.>]>

    # default tagger
    >>> from nltk.tagger import *
    >>> my_tagger = DefaultTagger('nn')
    >>> my_tagger.tag(text_token)
    >>> print text_token
    <[<John/nn>, <saw/nn>, <3/nn>, <polar/nn>, <bears/nn>, <./nn>]>

    # regex tagger
    >>> NN_CD_tagger = RegexpTagger([(r'^[0-9]+(.[0-9]+)?$', 'cd'), (r'.*', 'nn')])
    >>> NN_CD_tagger.tag(text_token)
    >>> print text_token
    <[<John/nn>, <saw/nn>, <3/cd>, <polar/nn>, <bears/nn>, <./nn>]>

    >>> from nltk.tagger import *
    >>> from nltk.corpus import brown

    # Tokenize ten texts from the Brown Corpus
    >>> train_tokens = []
    >>> for item in brown.items()[:10]:
    ...   train_tokens.append(brown.read(item))

    # Initialise and train a unigram tagger
    >>> mytagger = UnigramTagger(SUBTOKENS='WORDS')
    >>> for tok in train_tokens: 
    ...   mytagger.train(tok)

    # Construct the taggers
    >>> tagger1 = NthOrderTagger(1, SUBTOKENS='WORDS')       # first order tagger
    >>> tagger2 = UnigramTagger(SUBTOKENS='WORDS')           # zeroth order tagger
    >>> tagger3 = RegexpTagger([(r'^[0-9]+(.[0-9]+)?$', 'cd'), (r'.*', 'nn')], SUBTOKENS='WORDS')

    # Train the taggers
    >>> for tok in train_tokens:
    ...     tagger1.train(tok)
    ...     tagger2.train(tok)

    # Combine the taggers and view the results
    >>> tagger = BackoffTagger([tagger1, tagger2, tagger3])
    >>> tagger.tag(text_token)
    >>> print text_token
    <[<John/np>, <saw/vbd>, <3/cd>, <polar/nn>, <bears/nn>, <./.>]>


    '''

def test_chunking():
    '''
    >>> from nltk.tokenreader.tagged import ChunkedTaggedTokenReader
    >>> chunked_string = "[ the/DT little/JJ cat/NN ] sat/VBD on/IN [ the/DT mat/NN ]"
    >>> reader = ChunkedTaggedTokenReader(chunk_node='NP', SUBTOKENS='WORDS')
    >>> sent_token = reader.read_token(chunked_string)
    >>> print sent_token['TREE']
    (S:
      (NP: <the/DT> <little/JJ> <cat/NN>)
      <sat/VBD>
      <on/IN>
      (NP: <the/DT> <mat/NN>))
    

    '''


def _test():
    import doctest, test_code2
    return doctest.testmod(test_code2)

if __name__ == '__main__':
    _test()

