import nltk, re, pprint
from nltk import word_tokenize

class Corpus: 
    def __init__(self, f_name): 
        self.texts = {}
        self.choices = {'1': 'DoI', '2': 'Bible', '3': 'Poe', '4': 'Dickens', '5': 'Melville'}
        found = False
        chunk = []
        key = ""
        f = open(f_name, 'r')
        for line in f:
            m = re.match(r'^\+\s+(.*)$', line)
            if m:
                found = True
                key = m.group(1)
                continue
            if re.match(r'^-', line):
                found = False
            if found == True:
                chunk.append(line)
            if found == False and key:
                self.texts[key] = chunk
                chunk = []
                key = ""
                
    def choose(self): 
        print "Which text would you prefer?"
        print "For Declaration of Independence, type 1."
        print "For Genesis from the Bible, type 2."
        print "For The Raven by Poe, type 3." 
        print "For A Tale of Two Cities by Dickens, type 4."
        print "For Moby Dick by Melville, type 5."
        uinput = str(raw_input())
        
        self.choice = self.choices[uinput.rstrip()]
        return self.texts[self.choice]
    
    def choose_dictionary(self):
        print "Which dictionary would you prefer?"
        print "For Poe dictionary, type 1."
        print "For computer dictionary, type 2." 
        
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
    
    def s7(self, key):
        # look up text and use nltk to tokenize 
        f = open(text1)
        lines = f.read()
        tokens = nltk.word_tokenize(lines)
        words = [word.lower() for word in tokens if word.isalpha()]

        for w,pos in nltk.pos_tag(words):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                word_index = sorted_nouns.index(w)
                print(sorted_nouns[word_index + 7])
            else:
                print(w)
        
if __name__ == "__main__":
    c = Corpus('Texts.txt')
    print c.texts.keys()
    print c.choose()