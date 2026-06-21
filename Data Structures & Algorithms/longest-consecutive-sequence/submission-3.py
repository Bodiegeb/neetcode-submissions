class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for num in nums:
            curr = 1
            while num + 1 in numSet:
                curr += 1
                num += 1
            res = max(res, curr)
        return res