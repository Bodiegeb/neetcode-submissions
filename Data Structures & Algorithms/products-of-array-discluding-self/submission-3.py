class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        postfix = [0] * length
        res = [0] * length
        prefix[0] = postfix[length - 1] = 1
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        for i in range(length):
            res[i] = prefix[i] * postfix[i]
        return res
