class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        k = n
        while k:
            i = k%10
            s += i
            p*= i
            k //= 10
        if n%(s+p) == 0 :
            return True
        return False