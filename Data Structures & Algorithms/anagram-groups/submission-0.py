class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c={}
        for i in strs:
            w="".join(sorted(i))
            if w not in c:
                c[w]=[]
            c[w].append(i)
        return list(c.values())
        