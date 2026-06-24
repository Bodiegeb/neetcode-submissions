class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict

    def shortest(self, word1: str, word2: str) -> int: 
        w1 = -1
        w2 = -1
        minDis = math.inf
        for i in range(len(self.words)):
            if self.words[i] == word1:
                w1 = i
            if self.words[i] == word2:
                w2 = i
            if w1 != -1 and w2 != -1:
                minDis = min(minDis, abs(w2 - w1))
        return minDis
            
            


