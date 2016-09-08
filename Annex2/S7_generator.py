# Into command line: 
#1: cd ~/Documents/digital-oulipo/foo
#2: virtualenv -p /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 venv
#3: source venv/bin/activate

import nltk, re, pprint
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import inflect

class S7_Transformer:

    def __init__(self, sourcedict, sourcetext, offset):
        wnl = WordNetLemmatizer()
        porter = PorterStemmer()
        self.sourcetext = sourcetext
        self.offset = offset
        self.dict = []
        f = open(sourcedict) # opens file
        lines = f.read() # read all lines
        words = nltk.word_tokenize(lines) # tokenize words
        words = sorted(words, key=str.lower)

        for w,pos in nltk.pos_tag(words):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                self.update_dictionary(w) 
    
    def update_dictionary(self, word):
        if word not in self.dict:
            self.dict.append(word)
            self.dict = list(sorted(set(self.dict)))
        return self.dict
        
    def generate_text(self):
        wnl = WordNetLemmatizer()
        porter = PorterStemmer()
        f = open(self.sourcetext)
        lines = f.read()
        tokens = nltk.word_tokenize(lines)
        words = [word.lower() for word in tokens if word.isalpha()]

        for w,pos in nltk.pos_tag(words):
            if (pos == 'NN' or pos == 'NNP'):
                self.dict = self.update_dictionary(w)
                word_index = self.dict.index(w)
                r_index = min((word_index + self.offset), len(self.dict) - 1)
                print(self.dict[r_index])
            elif (pos == 'NNS' or pos == 'NNPS'):
                lemma = wnl.lemmatize(w) if wnl.lemmatize(w).endswith('e') else porter.stem(w)
                self.dict = self.update_dictionary(lemma)
                word_index = self.dict.index(lemma)
                p = inflect.engine()
                r_index = min((word_index + self.offset), len(self.dict) - 1)
                print(p.plural(self.dict[r_index]))
            else:
                print(w)
                
if __name__ == "__main__":
        
    def choose_dict(): 
        choices = {'1': 'Poe.txt', '2': 'King_James_Bible.txt', '3': 'InauguralAddressCorpus.txt', '4': 'MontyPython.txt', '5': '/usr/share/dict/words'}
        print("Which noun dictionary would you prefer?")
        print("For Edgar Allan Poe, type 1.")
        print("For King James Bible, type 2.")
        print("For Inaugural Address Corpus, type 3.") 
        print("For Monty Python and the Holy Grail, type 4.") # ditto
        print("For traditional dictionary, type 5.")
        choice = choices[input()]
        return choice

    def choose_sourcetext(): 
        choices = {'1': 'DoI.txt', '2': 'Bible.txt', '3': 'Raven.txt', '4': 'Dickens.txt', '5': 'Melville.txt'}
        print("Which text would you prefer?")
        print("For Declaration of Independence, type 1.")
        print("For Genesis from the Bible, type 2.")
        print("For The Raven by Poe, type 3.")
        print("For A Tale of Two Cities by Dickens, type 4.")
        print("For Moby Dick by Melville, type 5.")

        return choices[input()]
        
    def choose_offset():
        print("For an S+n, what would you like n to be?")
        
        return int(input())
        
    sourcedict = choose_dict()
    sourcetext = choose_sourcetext()
    offset = choose_offset()
    print(sourcedict, sourcetext, offset)
    
    my_dict = S7_Transformer(sourcedict, sourcetext, offset)
    my_dict.generate_text()