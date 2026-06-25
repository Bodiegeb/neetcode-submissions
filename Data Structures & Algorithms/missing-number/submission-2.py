class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        series_sum = int(n*(n+1)/2)
        arr_sum = sum(nums)
        return series_sum - arr_sum