def S7(words):
    print "Pick a word"
    word = str(raw_input())
    word_index = words.index(word)
    for word in words: 
        return words[word_index + 7]    

if __name__ == "__main__":
    words = open('/usr/share/dict/words', 'r').read().splitlines()
    print S7(words)