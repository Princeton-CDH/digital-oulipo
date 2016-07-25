import re

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
        
if __name__ == "__main__":
    c = Corpus('Texts.txt')
    print c.texts.keys()
    print c.choose()