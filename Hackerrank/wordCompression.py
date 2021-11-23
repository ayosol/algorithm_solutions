# Test for Pocket Gem

def compressWord(word, k):
    i, j = 0, 0
    while i < len(word):
        c = 1
        j = i + 1
        while j < len(word) and word[i] == word[j]:
            c += 1
            j += 1
        if c == k:
            word = word[0:i] + word[j:len(word)]
            i = -1
               
        i += 1
    return word