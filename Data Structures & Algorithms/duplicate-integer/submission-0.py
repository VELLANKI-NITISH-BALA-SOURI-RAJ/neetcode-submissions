class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        g=False
        for i in nums:
            if i in s:
                g=True
            else:
                s.add(i)
        return g
        