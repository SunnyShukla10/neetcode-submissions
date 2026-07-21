class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_dist = 0
        while l < r:
            min_height = min(heights[l], heights[r])
            max_dist = max(max_dist, min_height * (r-l))

            if min_height == heights[l]:
                l += 1
            else:
                r -= 1
        return max_dist