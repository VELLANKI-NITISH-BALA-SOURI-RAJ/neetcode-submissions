class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(','}':'{',']':'['}
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                if st[-1]!=pairs[i]:
                    return False

                st.pop()
        return len(st)==0