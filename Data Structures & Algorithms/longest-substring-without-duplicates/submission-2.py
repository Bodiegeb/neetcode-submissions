class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            longest = max(longest, r - l + 1)
            seen.add(s[r])
            r += 1
        return longest