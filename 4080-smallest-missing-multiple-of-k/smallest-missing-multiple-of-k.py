class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        l = k
        while i <len(nums):
            while i < len(nums) and nums[i] < k:
                i+=1
            if i< len(nums) and nums[i] == k:
                k+=l
            else:
                return k
        return k
