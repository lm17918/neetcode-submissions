class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=len(nums)-1
        count =0
        for i,n in enumerate(nums):
            if n ==val:
                print("     true", r) 
                while r >=0 and  nums[r]==val:
                    print("         while")
                    r-=1
                nums[i]=nums[r]
                r-=1
                
            else:
                count+=1
            print(nums)
        return count