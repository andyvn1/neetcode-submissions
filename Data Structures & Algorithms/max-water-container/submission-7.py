class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            distance = r - l
            if heights[l] < heights[r]:
                maxArea = max(maxArea, distance * heights[l])
                l += 1
            else:
                maxArea = max(maxArea, distance * heights[r])
                r -= 1
        return maxArea
        