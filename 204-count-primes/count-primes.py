class Solution:
    def countPrimes(self, n: int) -> int:
        l = [True] *(n)
        if n>0:
            l[0] = False
        if n> 1:
            l[1] = False
        for i in range(2,n):
            if l[i]:
                for j in range(i*2, n,i):
                    l[j] = False
        c = 0
        for i in l:
            if i == True:
                c+=1
        return c