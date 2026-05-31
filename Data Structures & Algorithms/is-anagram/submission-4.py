class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        w1 = {}
        w2 = {}

        for i in range(len(s)):
            w1[s[i]] = 1 + w1.get(s[i], 0)
            w2[t[i]] = 1 + w2.get(t[i], 0)
        return w1 == w2