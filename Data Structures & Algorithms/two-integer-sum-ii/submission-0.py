class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c={}
        for i,val in enumerate(numbers):
            y=target-val
            if y in c:
                return [c[y]+1,i+1]
            c[val]=i
        