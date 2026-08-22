class Solution(object):
    def smallestValue(self, n):
        k = n
        l = [True] * n
        l[0] = False
        if len(l)>1:
            l[1] = False
        s = 0
        c = 0
        for i in range(2,n):
            if l[i] :
                for j in range(i*2,n,i):
                    l[j] = False
                while n% i == 0:
                    s += i
                    n = n//i
                    c+=1
        if c == 0 :
            return n
        if s == k:
            return s
        return  self.smallestValue(s)