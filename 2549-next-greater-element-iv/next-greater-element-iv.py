class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack1 = []
        stack2 = []
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            while stack2 and nums[stack2[-1]] < nums[i]:
                idx = stack2.pop()
                ans[idx] = nums[i]
            temp = []
            
            while stack1 and nums[stack1[-1]] < nums[i]:
                temp.append(stack1.pop())
            
            while temp:
                stack2.append(temp.pop())
            stack1.append(i)
        return ans