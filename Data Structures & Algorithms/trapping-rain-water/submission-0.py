class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        p=[0]*n
        p[0]=height[0]
        s=[0]*n
        s[n-1]=height[n-1]
        for i in range(n):
            p[i]=max(p[i-1],height[i])
        for i in range(n-2,-1,-1):
            s[i]=max(s[i+1],height[i])
        i=0
        m=0
        while i<n:
            lm=p[i]
            rm=s[i]
            wl=min(lm,rm)
            if wl>0:
                m+=wl-height[i]
            i+=1
        return m