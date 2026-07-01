class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = defaultdict(int)
        for i in range(len(nums)):
            need = target - nums[i]
            if need in dictionary:
                return [dictionary[need], i]
            dictionary[nums[i]] = i 



# Goal: given an array return two indexes where the numbers sum up to the target
# Notices: they can be the same index, there can be the same numbers in list, the array is sorted
# Ideas: 
# - loop through every number in the list and return the index when it sums up to the target O(N^2) space O(1)
# - create a map with index and number and for eac number searcdh and return or add to map O(N) space O(N)
