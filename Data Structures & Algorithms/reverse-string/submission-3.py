class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lenght=len(s)
        for i in range (lenght//2):
            s[i],s[lenght-1-i]=s[lenght-1-i],s[i]