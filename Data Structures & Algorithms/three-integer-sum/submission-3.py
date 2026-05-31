class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = -nums[i]
                total = nums[j] + nums[k]
                if total == target:
                    part = [nums[i], nums[j], nums[k]]
                    if part not in res:
                        res.append(part)
                if total > target:
                    k -= 1
                else:
                    j += 1
        return res

