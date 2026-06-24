class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = {}
        for i, word in enumerate(wordsDict):
            if word not in self.words:
                self.words[word] = []
            self.words[word].append(i)

    def shortest(self, word1: str, word2: str) -> int: 
        list1 = self.words[word1]
        list2 = self.words[word2]
        minDis = (3 * 10**4) + 1
        i1 = 0
        i2 = 0
        while i1 < len(list1) and i2 < len(list2):
            minDis = min(minDis, abs(list1[i1] - list2[i2]))
            if list2[i2] < list1[i1]:
                i2 += 1
            else:
                i1 += 1
        return minDis
            
            


