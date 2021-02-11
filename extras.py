import random

# Formatting

sep = '<====================>'

# mad libs

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

def pnoun(amount):
    pnoun = [input('Pronoun: ') for _ in range (amount)]
    random.shuffle(pnoun)
    return pnoun