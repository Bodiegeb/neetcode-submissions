class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = {}
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            charSet[s[r]] = 1 + charSet.get(s[r], 0)
            maxFreq = max(maxFreq, charSet[s[r]])
            while (r - l + 1) - maxFreq > k:
                charSet[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res