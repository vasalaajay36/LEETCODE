class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            st = set()
            st.add(nums[i])
            s+=1
            for j in range(i-1,-1,-1):
                st.add(nums[j])
                s += len(st)**2
        return s