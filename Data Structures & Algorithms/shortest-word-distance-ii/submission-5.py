class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordsDict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int: 
        w1 = self.wordsDict[word1] # lists of possible words
        w2 = self.wordsDict[word2]
        dis = (3 * 10^4) + 1
        index1 = 0
        index2 = 0
        while index1 < len(w1) and index2 < len(w2):
            dis = min(dis, abs(w1[index1] - w2[index2]))
            if w1[index1] < w2[index2]:
                index1 += 1
            else:
                index2 += 1
        return dis
            
            



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