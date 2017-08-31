import pdb
import spacy

PROPN = 94
NNP = 475
NNPS = 476


ADJ = 82
JJ = 467     #
JJR = 468    # better
JJS = 469    # best

# ADJA
# ADJD
WDT = 494    # that, what
WPS = 496    # whose
PRPS = 480   # yours, hers
PDT = 478    # all, quite
AFX = 456    # non-

def get_proper_nouns(doc):
    ppns = []
    for word in doc:
        if word.pos == PROPN:
            ppns.append(word)
    return ppns

def get_proper_nouns_tags(doc):
    ppns = []
    for word in doc:
        if word.tag == NNP or word.tag == NNPS:
            ppns.append(word)
    return ppns

def get_adjectives(doc):
    adjs = {}
    adjs[JJ] = []
    adjs[JJR] = []
    adjs[JJS] = []
    adjs[PRPS] = []
    adjs[WPS] = []
    adjs[PRPS] = []
    adjs[PDT] = []
    adjs[WDT] = []
    adjs[AFX] = []
    adjs['other'] = []
    for word in doc:
        if word.pos == ADJ:
            if word.tag in adjs.keys():
                adjs[word.tag].append(word)
            else:
                adjs['other'].append(word)
    return adjs

def get_interesting_adjs(doc):
    adjectives_dictionary = get_adjectives(doc)
    return adjectives_dictionary[JJ]

def get_most_common(list_of_words):
    uniquely = {}
    for word in list_of_words:
        if word.string not in uniquely:
            uniquely[word.string] = 1
        else:
            uniquely[word.string] += 1
    return sorted(uniquely.items(), key=lambda x:x[1])

def get_avg_length(list_of_words):
    return float(sum(map(len, list_of_words))) / len(list_of_words)

def print_tags(word):
    print (word, word.tag_, word.tag, word.pos_, word.pos)

def print_all_heuristics(doc):
    print 'avg length: all words:', get_avg_length(doc)
    print 'avg length: all single word proper nouns:', \
                            get_avg_length(get_proper_nouns(doc))
    print 'avg length: descriptive adjectives:', \
                            get_avg_length(get_interesting_adjectives(doc))

if __name__ == '__main__':
    nlp = spacy.load('en')
    f = open('HarryPotter3-PrisonerAzkaban.txt')
    doc = nlp(unicode(f.read()))
    common_harry_p = get_most_common(get_interesting_adjs(doc))
    print common_harry_p
