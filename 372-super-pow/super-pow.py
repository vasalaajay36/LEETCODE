class Solution:
    mod = 1337
    
    def superPow(self, a: int, b: List[int]) -> int:
        num = 0
        res = 1
        for i in b:
            res = (res ** 10 * a**i)%self.mod

        return res
        #return self.fun(a,num)