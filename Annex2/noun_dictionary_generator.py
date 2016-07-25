# Into command line: 
#1: cd ~/Documents/digital-oulipo/foo
#2: virtualenv -p /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 venv
#3: source venv/bin/activate

# code to generate noun dictionary (sorted alphabetically, all lowercase) 

import nltk, re, pprint
from nltk import word_tokenize

text = '/usr/share/dict/words' # defines file, can choose any text or dictionary to generate noun dictionary 
f = open(text) # opens file
lines = f.read() # read all lines
words = nltk.word_tokenize(lines) # tokenize words
words = sorted(words, key=str.lower)
nouns = []

for w,pos in nltk.pos_tag(words):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        nouns.append(w)
sorted_nouns = list(sorted(set(nouns)))

# S+7 program: reads a text into nltk, tokenizes, and if word is not noun, print word, if word is noun, make substitution

text1 = 'DoI.txt'
text2 = 'Bible.txt'
text3 = 'Dickens.txt'
text4 = 'Poe.txt'
text5 = 'Melville.txt'

f = open(text1)
lines = f.read()
tokens = nltk.word_tokenize(lines)
words = [word.lower() for word in tokens if word.isalpha()]

for w,pos in nltk.pos_tag(words):
    if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
        word_index = sorted_nouns.index(w)
        if w is in sorted_nouns: # what on earth is the syntax for this??
            print(sorted_nouns[word_index + 7])
        else: 
            list(sorted(set(sorted_nouns.append(w))))
            print (sorted_nouns[word_index +7])
    else:
        print(w)

# for hw: figure out how to add words that aren't there to the dictionary and then find the S+7
# then, if I get that to work, find 
