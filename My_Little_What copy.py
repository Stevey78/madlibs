# My Little Pony Madlib

import extras as xs

# variables for madlib

noun = xs.noun(5)
adjs = xs.adjs(8)
verb = xs.verb(2)
pnoun = xs.pnoun(3)

pnoun1,pnoun2,pnoun3 = pnoun
adverb1 = input('adverb: ')
verb1,verb2 = verb
prep1 = input('preposition: ')
noun1,noun2,noun3,noun4,noun5 = noun
adjs1,adjs2,adjs3,adjs4,adjs5,adjs6,adjs7,adjs8 = adjs

# madlib

madlib = f'\nWhen I was {adjs1} I was too {adjs2} to make any {noun1}.\
\nSuch {adjs3} did not seem {prep1} the {noun2} it {verb1}.\
\nBut my {adjs4} {pnoun1}, you {verb2} up my {pnoun2}\
\nAnd now the {noun3} is {adjs5} {adverb1}, as {adjs6} {adjs7} {pnoun3}.\
\nAnd it\'s such a {adjs8} {noun4}.\n'

print(xs.sep)
print(madlib)
print(xs.sep)

input('Press ENTER to see the original')

original = '\nWhen I was young I was too busy to make any friends. \
\nSuch silliness did not seem worth the effort it expends. \
\nBut my little ponies, you opened my eyes \
\nAnd now the truth is crystal clear, as splendid summer skies. \
\nAnd it\'s such a wonderful surprise.\n'

print(xs.sep)
print(original)
print(xs.sep)


input('Press ENTER to quit')