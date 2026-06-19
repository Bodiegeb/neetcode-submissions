class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # add all decitions that include i
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # add all decitions that dont include i
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res