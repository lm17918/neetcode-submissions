class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=0
        if len(s)==0:
            return True
        for char in t:
            if s[l]==char:
                l+=1
                print(len(s))
                if l==len(s):
                    return True
        return False