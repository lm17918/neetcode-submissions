class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            print(l,r,"    ", numbers[r],numbers[l])
            if numbers[r]+numbers[l]==target:               
                return [l + 1, r + 1]
            elif numbers[r]+numbers[l] <target:
                l+=1
            else:
                r-=1
        return []
