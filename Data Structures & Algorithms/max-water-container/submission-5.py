class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_height_length = 0

        l, r = 0, len(heights) - 1

        while l < r:
            maximum_water = (r - l) * min(heights[l], heights[r])
            maximum_height_length = max(maximum_height_length, maximum_water)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maximum_height_length


        