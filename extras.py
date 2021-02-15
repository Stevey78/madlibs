import random

# Formatting

sep = '<========================================>'
words = ['animal','astronomy','baseball','beach','castles','clothes','driving','elements','family','farm','fish','furniture','halloween','human body','kitchen','maps','money','music','ocean','plants','presidents','queens','school','sex','shapes','spring','summer','theater','tools','US States','vacation','weather','winter']

# mad libs

def theme():
    print('Please choose words to fit the following theme: ')
    words = ['animal','astronomy','baseball','beach','castles','clothes','driving','elements','family','farm','fish','furniture','halloween','human body','kitchen','maps','money','music','ocean','plants','presidents','queens','school','sex','shapes','spring','summer','theater','tools','US States','vacation','weather','winter']
    x = random.choice(words)
    y = x.upper()
    print(y)

def noun(amount):
    noun = [input('Noun: ') for _ in range(amount)]
    random.shuffle(noun)
    return noun

def adjs(amount):
    adjs = [input('Adjective: ')for _ in range(amount)]
    random.shuffle(adjs)
    return adjs

def prep(amount):
    prep = [input('Preposition: ') for _ in range(amount)]
    random.shuffle(prep)
    return prep

def verb(amount):
    verb = [input('Verb: ') for _ in range(amount)]
    random.shuffle(verb)
    return verb

def adverb(amount):
    adverb = [input('Adverb: ') for _ in range(amount)]
    random.shuffle(adverb)
    return adverb

def pronoun(amount):
    pnoun = [input('Pronoun: ') for _ in range(amount)]
    random.shuffle(pnoun)
    return pnoun

def pluralnoun(amount):
    pluralnoun = [input('Plural Noun: ') for _ in range(amount)]
    random.shuffle(pluralnoun)
    return pluralnoun