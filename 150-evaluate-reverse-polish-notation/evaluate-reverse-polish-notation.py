class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()) :
                s.append(int(i))
            else:
                a = int(s.pop())
                b = int(s.pop()) 
                if i == '*':
                    s.append(a*b)
                elif i == '/':
                    s.append(int(b/a))
                elif i == '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(b-a)
        return s[0]