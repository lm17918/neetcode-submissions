class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g)==1:
            if g in s :
                return 1
        count=0
        s=sorted(s)
        for c in sorted(g):
            l=0
            while l< len(s):
                if s[l]>=c:
                    count+=1
                    s.pop(l)
                    break
                l+=1
        return count
