# WAP - Wet Ass Pussy Madlib

import extras as xs
import random
from prompt_toolkit import prompt
# from _typeshed import NoneType

# Variables
def word_s():
    words = []
    pnoun1 = (0, 'Plural Noun: ')
    noun1 = (1, 'Noun(building): ')
    noun2 = (2, 'Noun: ')
    noun3 = (3, 'Noun: ')
    adj1 = (4, 'Adjective: ')
    noun4 = (5, 'Noun: ')
    noun5 = (6, 'Noun(tool): ')
    noun6 = (7, 'Noun(tool): ')
    noun7 = (8, 'Noun: ')
    noun8 = (9, 'Noun(proper)')
    verb1 = (10, 'Verb(action): ')
    verb2 = (11, 'Verb: ') 
    noun9 = (12, 'Noun:')
    prep1 = (13, 'Preposition: ')
    prep2 = (14, 'Preposition: ')
    noun10 = (15, 'Noun: ')
    verb3 = (16, 'Verb: ')
    noun11 = (17, 'Noun: ')
    verb4 = (18, 'Verb: ')
    noun12 = (19, 'Noun: ')
    verb5 = (20, 'Verb: ')
    verb6 = (21, 'Verb: ')
    noun13 = (22, 'Noun: ')
    verb7 = (23, 'Verb: ')

    questions = [pnoun1, noun1, noun2, noun3, adj1, noun4, noun5, noun6, noun7,
    noun8, verb1, verb2, noun9, prep1, prep2, noun10, verb3, noun11,
    verb4, noun12, verb5, verb6, noun13, verb7]
    random.shuffle(questions)

    for id, prompt in questions:
        words[id] = input(prompt)

word_s()

madlib = f'\n{pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1} (Hol\' up)\
\nI said certified {noun2}, seven days a week\
\n{adj1}-{noun3} {noun4}, make that {noun7} game weak, woo (Ah)\
\n\
\nYeah, yeah, yeah, yeah\
\nYeah, you fuckin\' with some {adj1}-{noun3} {noun4}\
\nBring a {noun5} and a {noun6} for this {adj1}-{noun3} {noun4}\
\nGive me everything you got for this {adj1}-{noun3} {noun4}\
\n\
\n{verb1} it up, {noun8}, {verb2} a {noun9}\
\nExtra {prep1} and extra {prep2}\
\nPut this {noun4} right in your {noun10}\
\n{verb3} your {noun11} like a credit card\
\nHop on {noun12}, I wanna {verb4}\
\nI do a kegel while it\'s inside\
\nSpit in my mouth, look in my eyes\
\nThis {noun4} is {adj1}, come take a {verb5}\
\nTie me up like I\'m {verb6}\
\nLet\'s {verb7}, I\'ll wear a {noun13}\
\nI want you to park that big Mack truck right in this little garage\
\nMake it cream, make me scream\
\nOut in public, make a scene\
\nI don\'t cook, I don\'t clean\
\nBut let me tell you how I got this ring (Ayy, ayy)\
\n\
\nGobble me, swallow me, drip down the side of me (Yeah)\
\nQuick, jump out \'fore you let it get inside of me (Yeah)\
\nI tell him where to put it, never tell him where I\'m \'bout to be (Huh)\
\nI\'ll run down on him \'fore I have a {noun8} runnin\' me (Pow, pow, pow)\
\nTalk your shit, bite your lip (Yeah)\
\nAsk for a car while you ride that dick (While you ride that dick)\
\nYou really ain\'t never gotta fuck him for a thang (Yeah)\
\nHe already made his mind up \'fore he came (Ayy, ah)\
\nNow get your boots and your coat for this {adj1}-{noun3} {noun4} (Ah, ah, ah)\
\nHe bought a phone just for pictures of this {adj1}-{noun3} {noun4} (Click, click, click)\
\nPaid my tuition just to kiss me on this {adj1}-{noun3} {noun4} (Mwah, mwah, mwah)\
\nNow make it rain if you wanna see some {adj1}-{noun3} {noun4} (Yeah, yeah)\
\n\
\nLook, I need a hard hitter, need a deep stroker\
\nNeed a Henny drinker, need a weed smoker\
\nNot a garter snake, I need a king cobra\
\nWith a hook in it, hope it lean over\
\nHe got some money, then that\'s where I\'m headed\
\n{noun4} A1 just like his credit\
\nHe got a beard, well, I\'m tryna {adj1} it\
\nI let him taste it, now he diabetic\
\nI don\'t wanna spit, I wanna gulp\
\nI wanna gag, I wanna choke\
\nI want you to touch that lil\' dangly thing that swing in the back of my throat\
\nMy head game is fire, punani Dasani\
\nIt\'s goin\' in dry and it\'s comin\' out soggy\
\nI ride on that thing like the cops is behind me (Yeah, ah)\
\nI spit on his mic and now he tryna sign me, woo\
\n\
\nYour honor, I\'m a {noun2} bitch, handcuffs, leashes\
\nSwitch my wig, make him feel like he cheatin\'\
\nPut him on his knees, give him somethin\' to believe in\
\nNever lost a fight, but I\'m lookin\' for a beatin\' (Ah)\
\nIn the food chain, I\'m the one that eat ya\
\nIf he ate my {noun3}, he\'s a bottom-feeder\
\nBig D stand for big demeanor\
\nI could make ya bust before I ever meet ya\
\nIf it don\'t hang, then he can\'t bang\
\nYou can\'t hurt my feelings, but I like pain\
\nIf he fuck me and ask "Whose is it?"\
\nWhen I ride the dick, I\'ma spell my name, ah\
\n\
\nYeah, yeah, yeah\
\nYeah, you fuckin\' with some {adj1}-{noun3} {noun4}\
\nBring a {noun5} and a {noun6} for this {adj1}-{noun3} {noun4}\
\nGive me everything you got for this {adj1}-{noun3} {noun4}\
\nNow from the top, make it drop, that\'s some {adj1}-{noun3} {noun4}\
\nNow get a {noun5} and a {noun6}, that\'s some {adj1}-{noun3} {noun4}\
\nI\'m talkin\' wap, wap, wap, that\'s some {adj1}-{noun3} {noun4}\
\nMacaroni in a pot, that\'s some {adj1}-{noun3} {noun4}, huh\
\n\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\nThere\'s some {pnoun1} in this {noun1}\
\n'

# Original

orig = '\nWhores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house (Hol\' up)\
\nI said certified freak, seven days a week\
\nWet-ass pussy, make that pullout game weak, woo (Ah)\
\n\
\nYeah, yeah, yeah, yeah\
\nYeah, you fuckin\' with some wet-ass pussy\
\nBring a bucket and a mop for this wet-ass pussy\
\nGive me everything you got for this wet-ass pussy\
\n\
\nBeat it up, nigga, catch a charge\
\nExtra large and extra hard\
\nPut this pussy right in your face\
\nSwipe your nose like a credit card\
\nHop on top, I wanna ride\
\nI do a kegel while it\'s inside\
\nSpit in my mouth, look in my eyes\
\nThis pussy is wet, come take a dive\
\nTie me up like I\'m surprised\
\nLet\'s roleplay, I\'ll wear a disguise\
\nI want you to park that big Mack truck right in this little garage\
\nMake it cream, make me scream\
\nOut in public, make a scene\
\nI don\'t cook, I don\'t clean\
\nBut let me tell you how I got this ring (Ayy, ayy)\
\n\
\nGobble me, swallow me, drip down the side of me (Yeah)\
\nQuick, jump out \'fore you let it get inside of me (Yeah)\
\nI tell him where to put it, never tell him where I\'m \'bout to be (Huh)\
\nI\'ll run down on him \'fore I have a nigga runnin\' me (Pow, pow, pow)\
\nTalk your shit, bite your lip (Yeah)\
\nAsk for a car while you ride that dick (While you ride that dick)\
\nYou really ain\'t never gotta fuck him for a thang (Yeah)\
\nHe already made his mind up \'fore he came (Ayy, ah)\
\nNow get your boots and your coat for this wet-ass pussy (Ah, ah, ah)\
\nHe bought a phone just for pictures of this wet-ass pussy (Click, click, click)\
\nPaid my tuition just to kiss me on this wet-ass pussy (Mwah, mwah, mwah)\
\nNow make it rain if you wanna see some wet-ass pussy (Yeah, yeah)\
\n\
\nLook, I need a hard hitter, need a deep stroker\
\nNeed a Henny drinker, need a weed smoker\
\nNot a garter snake, I need a king cobra\
\nWith a hook in it, hope it lean over\
\nHe got some money, then that\'s where I\'m headed\
\nPussy A1 just like his credit\
\nHe got a beard, well, I\'m tryna wet it\
\nI let him taste it, now he diabetic\
\nI don\'t wanna spit, I wanna gulp\
\nI wanna gag, I wanna choke\
\nI want you to touch that lil\' dangly thing that swing in the back of my throat\
\nMy head game is fire, punani Dasani\
\nIt\'s goin\' in dry and it\'s comin\' out soggy\
\nI ride on that thing like the cops is behind me (Yeah, ah)\
\nI spit on his mic and now he tryna sign me, woo\
\n\
\nYour honor, I\'m a freak bitch, handcuffs, leashes\
\nSwitch my wig, make him feel like he cheatin\'\
\nPut him on his knees, give him somethin\' to believe in\
\nNever lost a fight, but I\'m lookin\' for a beatin\' (Ah)\
\nIn the food chain, I\'m the one that eat ya\
\nIf he ate my ass, he\'s a bottom-feeder\
\nBig D stand for big demeanor\
\nI could make ya bust before I ever meet ya\
\nIf it don\'t hang, then he can\'t bang\
\nYou can\'t hurt my feelings, but I like pain\
\nIf he fuck me and ask "Whose is it?"\
\nWhen I ride the dick, I\'ma spell my name, ah\
\n\
\nYeah, yeah, yeah\
\nYeah, you fuckin\' with some wet-ass pussy\
\nBring a bucket and a mop for this wet-ass pussy\
\nGive me everything you got for this wet-ass pussy\
\nNow from the top, make it drop, that\'s some wet-ass pussy\
\nNow get a bucket and a mop, that\'s some wet-ass pussy\
\nI\'m talkin\' wap, wap, wap, that\'s some wet-ass pussy\
\nMacaroni in a pot, that\'s some wet-ass pussy, huh\
\n\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\nThere\'s some whores in this house\
\n'

print(xs.sep)
print(madlib)
print(xs.sep)
input('Press ENTER to see original')
print(xs.sep)
print(orig)
print(xs.sep)
input('Press ENTER to exit')