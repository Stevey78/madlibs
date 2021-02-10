# My Little Pony Madlib

import extras as xs

# variables for madlib

adj1, adj2, adj3, adj4, adj5, adj6, adj7, adj8 = input('Enter 8 different adjectives: ').split(',')
noun1, noun2, noun3, noun4, noun5 = input('Enter 5 different nouns: ').split(',')
prep1 = input('Enter 1 preposition: ')
verb1, verb2 = input('Enter 2 different verbs: ').split(',')
adverb1 = input('Enter 1 adverb: ')
pnoun1, pnoun2, pnoun3 = input('Enter 3 different pronouns: ').split(',')

# madlib

madlib = f'\nWhen I was {adj1} I was too {adj2} to make any {noun1}.\
\nSuch {adj3} did not seem {prep1} the {noun2} it {verb1}.\
\nBut my {adj4} {pnoun1}, you {verb2} up my {pnoun2}\
\nAnd now the {noun3} is {adj5} {adverb1}, as {adj6} {adj7} {pnoun3}.\
\nAnd it\'s such a {adj8} {noun4}.\n'

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