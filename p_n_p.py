# Pride & Prejudice (Jane Austen)


# It is a truth universally acknowledged, that a single man in possession
# of a good fortune must be in want of a wife. However little known the feeling
# or views of such a man may be on his first entering a neighbourhood, this
# truth is so well fixed in the minds of the surrounding families, that he is
# considered as the rightful property of some one or other of their daughters.

import extras as xs

xs.theme()
noun1,noun2,noun3,noun4,noun5,noun6,noun7,noun8,noun9 = xs.noun(9)
adj1,adj2 = xs.adjs(2)
adverb1 = input('Enter an adverb: ')
pluralnoun1,pluralnoun2,pluralnoun3,pluralnoun4 = xs.pluralnoun(4)

madlib = f'\nIt is a {noun1} universally acknowledged, that a {adj1} {noun2} in possession\
\n of a {adj2} {noun3} must be in want of a {noun4}. However {adverb1} known the {noun5}\
\n or {pluralnoun1} of such a {noun6} may be on his first entering a {noun7}, this\
\n {noun8} is so well fixed in the {pluralnoun2} of the surrounding {pluralnoun3}, that he is\
\n considered as the rightful {noun9} of some one or other of their {pluralnoun4}.\n'

print(xs.sep)
print(madlib)
print(xs.sep)