class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        k = 0
        s = []
        for i in range(len(pushed)):
            s.append(pushed[i])
            while s and s[-1] == popped[k]:
                s.pop()
                k+=1
        if s:
            return False
        return True

        