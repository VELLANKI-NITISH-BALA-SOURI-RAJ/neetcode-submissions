from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        m = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = min(heights[i], heights[j]) * (j - i)
                m = max(m, area)

        return m