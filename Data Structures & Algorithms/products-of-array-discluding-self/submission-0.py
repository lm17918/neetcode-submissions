
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        prefix = 1
        for i in range(n):
            out[i] = prefix          # tutto a sinistra di i
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix         # moltiplica per tutto a destra di i
            suffix *= nums[i]

        return out
