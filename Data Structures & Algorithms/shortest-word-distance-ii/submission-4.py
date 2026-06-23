class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsdict = wordsDict

    def shortest(self, word1: str, word2: str) -> int: 
        w1 = -1
        w2 = -1
        distance = (3 * 10^4) + 1
        for i in range(len(self.wordsdict)):
            if self.wordsdict[i] == word1:
                w1 = i
            if self.wordsdict[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                distance = min(distance, abs(w2 - w1))
        return distance
            
            



# GOAL: create class where stores an arra of wordsDict 
# then function that returns shortest distance between two given words

# OBSERVATIONS: 
# - always in wordsDict
# - can have duplicate words
# - are not the same word1

# IDEAS: 1. keep wordsdict then search thorugh each word distance between each other
# 2. make a dicitonary with the positions then go through those indexes
# 
# 1. keep wordsDict in an arry, look thorugh each word if its the word update index and check if min 
#  approach init: O(1) shortest: O(N) 
# pros: if you are creating the these worddistances more than you are finding shortest

# 2. make a dicitonary with all the indices then then just go thorugh those indices init: O(N) shortest: O(K * M)
# opposite