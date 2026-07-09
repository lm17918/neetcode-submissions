class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1 
        n=0
        out=-1
        for i,h in enumerate(haystack):
            if needle[0] ==h:
                n=0
                j=i
                while n<=len (needle)-1:
                    if haystack[j]!=needle[n]:
                        break
                    elif n ==len (needle)-1:
                        return i
                    n+=1
                    j+=1
        return out
