class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=defaultdict(list)
        for s in strs:
            sort="".join(sorted(s))
            out[sort].append(s)
        outlist=[]
        for o in out.values():
            outlist.append(o)
        return outlist
