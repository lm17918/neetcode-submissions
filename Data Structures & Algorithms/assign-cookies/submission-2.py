class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        s=sorted(s)
        for c in sorted(g):
            l=0
           # print("c ",c)
            while l< len(s):
               # print("     l ",l)
                if s[l]>=c:
                    count+=1
                    s.pop(l)
              #      print("     s ",s)
                    break
                l+=1
        return count
