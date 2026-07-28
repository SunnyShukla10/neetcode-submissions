class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        max_area = 0
        while i < j:
            diff = j - i

            if heights[i] > heights[j]:
                max_area = max(max_area, diff * heights[j])
                j -= 1
            else:
                max_area = max(max_area, diff * heights[i])
                i += 1

        return max_area