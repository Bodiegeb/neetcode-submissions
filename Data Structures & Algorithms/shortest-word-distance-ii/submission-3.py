class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        w1 = -1
        w2 = -1
        shortest = len(self.wordsDict)
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] == word1:
                w1 = i
            elif self.wordsDict[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                shortest = min(shortest, abs(w1 - w2))
        return shortest



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# GOAL: create a class that holds a dictionary off words and that returns the shortest distacne between 2 words in the dictionary
# OBSERVATIONS: you can have duplicate words, word1 and 2 are in worddict, they wont be the same only
# 5k calls so O(N) i think is good time complexty
# APPROACH:
# copy the dictionary -