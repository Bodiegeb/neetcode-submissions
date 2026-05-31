class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                curr = (r - l) * heights[l]
                l += 1
            else:
                curr = (r - l) * heights[r]
                r -= 1
            maxA = max(maxA, curr)

        return maxA