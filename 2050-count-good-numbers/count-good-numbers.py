class Solution:
    mod = 10 **9 + 7
    def fun(self,a,n):
        if n == 0:
            return 1
        half = self.fun(a,n//2)
        if n %2 == 1:
            return (a * half* half) %self.mod
        return (half * half) % self.mod

        
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n//2
        return (self.fun(5,even)* self.fun(4,odd))%self.mod