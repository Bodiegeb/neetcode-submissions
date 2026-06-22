class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordsDict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.wordsDict[word1]
        indices2 = self.wordsDict[word2]
        min_distance = (3 * 10**4) + 1
        p_1 = 0
        p_2 = 0
        # greedy find the minimun distance
        while p_1 < len(indices1) and p_2 < len(indices2):
            index1 = indices1[p_1]
            index2 = indices2[p_2]
            min_distance = min(min_distance, abs(index1 - index2))
            if index1 < index2:
                p_1 +=1
            else:
                p_2 += 1
        return min_distance



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# GOAL: create a class that holds a dictionary off words and that returns the shortest distacne between 2 words in the dictionary
# OBSERVATIONS: you can have duplicate words, word1 and 2 are in worddict, they wont be the same only
# 5k calls so O(N) i think is good time complexty
# APPROACH:
# copy the dictionary -