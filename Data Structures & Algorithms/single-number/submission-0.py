class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            h[i]=h.get(i,0)+1
        l=min(h.values())
        p=[k for k , v in h.items() if v==l ]
        return p[0]
        
        