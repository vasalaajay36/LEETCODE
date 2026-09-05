class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx = [min(nums)]* len(nums)
        m ,l = 0,max(nums)
        mn = [max(nums)]* len(nums)
        for i in range(len(nums)):
            mx[i] = max(m,nums[i])
            m = mx[i]
        for i in range(len(nums)-1,-1,-1):
            mn[i] = min(l,nums[i])
            l = mn[i]
        for i in range(len(nums)):
            if mx[i]- mn[i] <= k:
                return i
        return -1