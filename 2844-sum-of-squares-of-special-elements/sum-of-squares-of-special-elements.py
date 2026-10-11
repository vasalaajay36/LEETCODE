class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        val = 0
        for i in range(n):
            if n%(i+1) == 0:
                val += nums[i]**2
        return val
        