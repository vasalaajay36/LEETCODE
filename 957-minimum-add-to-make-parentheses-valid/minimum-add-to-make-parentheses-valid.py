class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    c+=1
        return c + len(stack)
        