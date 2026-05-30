from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        m = 0
        l=0
        r=n-1
        while l<r:
            a=min(heights[l],heights[r])*(r-l)
            m=max(m,a)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return m
