class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        m = 0
        xor = 0
        mx = max(nums)
        for i in nums:
            xor ^= i

        if xor :
            return len(nums)
        if mx == 0:
            return 0
        return len(nums)-1
        