class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        if not nums:
            return 0
        nums=sorted(set(nums))
        c=1
        m=1
        for i in range(1,len(nums)):
            if (nums[i]-nums[i-1]) == 1:
                c+=1
            else:
                c=1
            m=max(c,m)
        return m