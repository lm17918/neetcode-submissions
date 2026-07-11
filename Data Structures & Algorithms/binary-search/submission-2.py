class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: 
            return -1
        l,r=0,len(nums)
        while l < r:
            mid=l+(r-l)//2
            if target<nums[mid]:#<>
                r=mid
            elif target>nums[mid]:#<>
                l=mid+1
            else:
                return mid
        return -1
