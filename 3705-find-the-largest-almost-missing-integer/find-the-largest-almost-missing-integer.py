class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == k :
            return max(nums)
        if k ==1:
            if max(nums) == min(nums):
                return -1
            nums.sort()
            l = len(nums)-1
            while l >= 0:
                if nums.count(nums[l]) == 1:
                    return nums[l]
                l-=1
            return -1
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] in nums[1:]:
            if nums[-1] in nums[:-1]:
                return -1
            return nums[-1]
        if nums[-1] in nums[:-1]:
            if nums[0] in nums[1:]:
                return -1
            else:
                return nums[0]
        return max(nums[0],nums[-1])