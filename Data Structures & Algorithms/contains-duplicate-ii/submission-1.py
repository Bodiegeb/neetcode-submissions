class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = {}
        for i, num in enumerate(nums):
            if num in numbers and abs(numbers[num] - i) <= k:
                return True
            numbers[num] = i
        return False