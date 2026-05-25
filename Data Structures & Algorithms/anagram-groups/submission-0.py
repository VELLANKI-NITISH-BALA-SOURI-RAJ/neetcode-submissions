class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c={}
        for e in strs:
            s="".join(sorted(e))
            if s not in c:
                c[s]=[]
            c[s].append(e)
        return list(c.values())
