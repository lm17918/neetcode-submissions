class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s: 
            return 0
        lent= len(t)
        lens= len(s)
        idxs=0
        idxt=0

        while idxt  <lent and idxs  <lens:
            if s[idxs]== t[idxt]:
                idxs+=1
                idxt+=1
            else:
                 idxs+=1
        

        return lent-idxt



