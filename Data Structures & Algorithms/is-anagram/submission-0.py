class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h=sorted(s)
        l=sorted(t)
        return h==l