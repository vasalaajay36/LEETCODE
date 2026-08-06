class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n:
            a = n
            p = 1
            while a:
                p *= a%10
                a = a//10
            if p == 0:
                return n
            elif  p%t == 0:
                return n
            n+=1
        