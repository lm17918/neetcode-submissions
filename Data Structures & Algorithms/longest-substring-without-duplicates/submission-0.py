class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        maxlenght=0
        left=0
        right=0
        for c in s:
            while c in seen:
                seen.pop(0)
            seen.append(c)
            maxlenght = max(maxlenght,len(seen)) 
        return maxlenght
