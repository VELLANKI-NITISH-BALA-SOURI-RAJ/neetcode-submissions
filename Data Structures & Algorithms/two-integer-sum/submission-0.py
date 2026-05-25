class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i , val in enumerate(nums):
            y=target-val
            if y in c:
                return [c[y], i]
            c[val]=i
        