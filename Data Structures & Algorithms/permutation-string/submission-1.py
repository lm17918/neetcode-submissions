class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenghtsub= len(s1) 
        for i in range (0,len(s2)):
            subst=  s2[i:i+lenghtsub]            
            if len(subst)<lenghtsub:
                continue

            print(subst, s1)
            if sorted(subst)== sorted(s1):
                return True
        return False
