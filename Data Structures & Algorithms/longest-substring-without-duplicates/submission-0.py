class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxLen = 0
        seen= set()
        while (end < len(s)):
            while(s[end] in seen):
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            end+=1
            maxLen = max(maxLen, end - start )
        return maxLen