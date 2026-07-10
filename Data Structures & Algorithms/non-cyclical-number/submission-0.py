class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        return self.check(n,seen)


    def check (self, listn:list,seen:set)-> bool:
        s= [int(numb) for numb in list(str(listn))]
        s= sum([numb*numb for numb in s])
        if s== 1:
            return True
        elif s in seen:
            return False
        else:
            seen.add(s)
            return self.check(s,seen)