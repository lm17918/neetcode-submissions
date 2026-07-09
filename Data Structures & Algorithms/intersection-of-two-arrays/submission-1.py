class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out= set()
        for n in nums1:
            if n in nums2:
                out.add(n)
        return list(out)