class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], target)
            elif target < matrix[mid][0] :
                r = mid - 1
            else:
                l = mid + 1
        return False


    def binarySearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return True
        return False
