class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            combined = numbers[l] + numbers[r]
            if(combined == target):
                return [l + 1, r + 1]
            if(combined > target):
                r -= 1
            if(combined < target):
                l += 1
        return [0,0]