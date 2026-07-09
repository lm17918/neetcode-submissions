class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap=defaultdict(int)
        for v in s:
            hashmap[v] = hashmap.get(v, 0) + 1
        print(hashmap)
        for v in t:
            if v not in hashmap:
                return False
            hashmap[v]-=1
            if hashmap[v]<0:
                return False
        return True