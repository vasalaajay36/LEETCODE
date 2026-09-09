class Solution:
    def countCommas(self, n: int) -> int:
        s = 0
        c = 1
        if n <1000:
            return 0
        for i in range(6,19,3):
            val = 10 ** i
            if val > n :
                s += (n - (10**(i-3))+1)*c
                break
            s += (val - 10**(i-3) ) *c
            c+=1
        return s
