class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res

# couple different ways
# O(N^2): for each number find if it has same number
# O(N) but O(N) space use a hasSet but add if seen then remove it not seen and whatever is left is number
#  O(N) but O(1) use XOR opporator its cummalitve so it will keep whatever number appears once