class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        premutes = []
        def backtrack(pick):
            if len(premutes) == len(nums):
                res.append(premutes.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    premutes.append(nums[i])
                    pick[i] = True
                    backtrack(pick)
                    pick[i] = False
                    premutes.pop()
        
        backtrack([False] * len(nums))
        return res


            