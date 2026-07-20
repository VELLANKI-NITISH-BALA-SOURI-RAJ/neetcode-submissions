class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=1
        r=1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=res[i]*l
            l=l*nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*r
            r=r*nums[i]
        return res