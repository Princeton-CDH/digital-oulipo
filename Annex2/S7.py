import nltk

def W7(words):
    print "Pick a word"
    word = str(raw_input())
    word_index = words.index(word)
    for word in words: 
        return words[word_index + 7]  
        
def S7(text, words): 
    text = "The quick brown fox jumps over the lazy dog."  
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    for token in text:     
    

if __name__ == "__main__":
    words = open('/usr/share/dict/words', 'r').read().splitlines()
    print S7(words)