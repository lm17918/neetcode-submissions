class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        hashmap={}
        treshold= len(nums)/2
        nums=sorted(nums)

        for n in nums:
            if n not in hashmap:
                hashmap[n]=1
            else:
                hashmap[n]+=1
                if hashmap[n]>treshold:
                    return n 
