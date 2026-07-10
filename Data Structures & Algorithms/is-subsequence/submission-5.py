class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        length = len(s)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == length