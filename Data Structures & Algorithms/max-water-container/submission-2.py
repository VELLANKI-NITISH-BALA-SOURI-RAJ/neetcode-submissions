class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        ma=0
        while l<r:
            m=min(heights[l],heights[r])*(r-l)
            ma=max(ma,m)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1

            
        return ma
        