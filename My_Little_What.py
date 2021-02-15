# My Little Pony Madlib

import extras as xs
import random

# variables for madlib

xs.theme()
# print('Please choose word to fit this theme:')
# word = xs.words
# x = random.choice(word)
# y = x.upper()
# print(y)

noun = xs.noun(9)
adjs = xs.adjs(6)
verb = xs.verb(2)


verb1,verb2 = verb
noun1,noun2,noun3,noun4,noun5,noun6,noun7,noun8,noun9 = noun
adjs1,adjs2,adjs3,adjs4,adjs6,adjs8 = adjs
adjs5 = input('2 word Adjective: ')

# madlib

madlib = f'\nWhen I was {adjs1} I was too {adjs2} to make any {noun1}.\
\nSuch {noun2} did not seem {adjs3} the {noun3} it {verb1}.\
\nBut my {adjs4} {noun4}, you {verb2} up my {noun5}\
\nAnd now the {noun6} is {adjs5}, as {adjs6} {noun7} {noun8}.\
\nAnd it\'s such a {adjs8} {noun9}.\n'

print(xs.sep)
print(madlib)
print(xs.sep)

input('Press ENTER to see the original')

original = '\nWhen I was young I was too busy to make any friends. \
\nSuch silliness did not seem worth the effort it expends. \
\nBut my little ponies, you opened up my eyes \
\nAnd now the truth is crystal clear, as splendid summer skies. \
\nAnd it\'s such a wonderful surprise.\n'

print(xs.sep)
print(original)
print(xs.sep)


input('Press ENTER to quit')