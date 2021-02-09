# My Little Pony Madlib

import extras as xs

# variables for madlib



adj1 = input('Adjective: ')
adj2 = input('Adjective: ')
noun1 = input('Noun: ')
adj3 = input('Adjective: ')
prep1 = input('Preposition: ')
noun2 = input('Noun: ')
verb1 = input('Verb: ')
adj4 = input('Adjective: ')
pnoun1 = input('Plural Noun: ')
verb2 = input('Verb: ')
pnoun2 = input('Plural Noun: ')
noun3 = input('Noun: ')
adj5 = input('Noun: ')
adverb1 = input('Adverb: ')
adj6 = input('Adjective: ')
adj7 = input('Adjective: ')
pnoun3 = input('Adjective: ')
adj8 = input('Adjective: ')
noun4 = input('Noun: ')

# madlib

madlib = f'\nWhen I was {adj1} I was too {adj2} to make any {noun1}. \nSuch {adj3} did not seem {prep1} the \
{noun2} it {verb1}. \nBut my {adj4} {pnoun1}, you {verb2} up my {pnoun2} \nAnd \
now the {noun3} is {adj5} {adverb1}, as {adj6} {adj7} {pnoun3}. \nAnd \
it\'s such a {adj8} {noun4}.\n'


# Original
original = '\nWhen I was young I was too busy to make any friends. \
\nSuch silliness did not seem worth the effort it expends. \
\nBut my little ponies, you opened my eyes \
\nAnd now the truth is crystal clear, as splendid summer skies. \
\nAnd it\'s such a wonderful surprise.\n'

print(xs.sep)
print(madlib)
print(xs.sep)

input('Press ENTER to see the original')

print(xs.sep)
print(original)
print(xs.sep)

# print(xs.madlib)

input('Press ENTER to quit')


