class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
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
