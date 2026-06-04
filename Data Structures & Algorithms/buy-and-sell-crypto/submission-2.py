class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        l=0
        r=1
        n=len(prices)
        while r<n:
            s=0
            if prices[r]>prices[l]:
                s+=prices[r]-prices[l]
                m=max(m,s)
            else:
                l=r
            r+=1
            
        return m

        