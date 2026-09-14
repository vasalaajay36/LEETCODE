
class Solution:
    def minInsertions(self, s: str) -> int:
        c = 0
        stack = []
        k = 0
        n = len(s)
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if i+1 <n and stack and s[i+1] == ')':
                    i+=1
                    stack.pop()
                elif stack and i+1<n and s[i+1] != ')':
                    c+=1
                    stack.pop()
                elif len(stack) == 0 and i+1 < n and s[i+1] == ')':
                    c+=1
                    i+=1
                elif len(stack) == 0 and i+1 <n and s[i+1] != ")":
                    c+=2
                elif i+1 == n :
                    if stack and s[i] == ')':
                        c+=1 
                        stack.pop()
                    elif len(stack) == 0 and s[i] == ")":
                        c+=2
            i+=1
        if stack:
            c+= len(stack)*2
        return c