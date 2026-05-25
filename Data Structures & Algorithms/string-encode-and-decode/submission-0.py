class Solution:

    def encode(self, strs: List[str]) -> str:
        r=""
        for s in strs:
            l=len(s)
            r=r+str(l)
            r=r+"#"
            r=r+s
        return r



    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i< len(s):
            j=i
            #find #
            while s[j]!='#':
                j+=1
            #len
            le=int(s[i:j])
            j+=1
            w=s[j:j+le]
            res.append(w)
            i=j+le
        return res

