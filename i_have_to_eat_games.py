# Hunger Games Mad Lib

# The rules of the Hunger Games are simple. In punishment for
# the uprising, each of the twelve districts must provide one
# girl and one boy, called tributes, to participate. The
# twenty-four tributes will be imprisoned in a vast outdoor
# arena that could hold anything from a burning desert to a
# frozen wasteland. Over a period of several weeks, the competitors
# must fight to the death. The last tribute standing wins.

import extras as xs
import random

print('Please choose word to fit this theme:')
word = xs.words
x = random.choice(word)
y = x.upper()
print(y)

pluralnoun1,pluralnoun2,pluralnoun3,pluralnoun4,pluralnoun5 = xs.pluralnoun(5)
propernoun_x2 = input('Enter a 2 word proper noun: ')
adj1,adj2 = xs.adjs(2)
noun1,noun2,noun3,noun4,noun5,noun6,noun7,noun8,noun9,noun10 = xs.noun(10)
number = input('Enter a number 1-24: ')
verb1,verb2,verb3,verb4 = xs.verb(4)
number2digits = input('Enter a number 10-99: ')
pluralverb = input('Enter a plural verb: ')


madlib = f'\nThe {pluralnoun1} of the {propernoun_x2} are {adj1}. In {noun1} for\
\nthe {noun2}, each of the {number} {pluralnoun2} must provide one\
\n{noun3} and one {noun4}, called {pluralnoun3}, to {verb1}. The\
\n{number2digits} {pluralnoun3} will be {verb2} in a vast {adj2}\
\n{noun5} that could {verb3} anything from a burning {noun6} to a\
\nfrozen {noun7}. Over a {noun8} of several {pluralnoun4}, the {pluralnoun5}\
\nmust {verb4} to the {noun9}. The last {noun10} standing {pluralverb}.\n'


print(xs.sep)
print(madlib)
print(xs.sep)