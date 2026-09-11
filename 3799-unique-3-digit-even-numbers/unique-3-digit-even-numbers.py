class Solution:
    def totalNumbers(self, d: List[int]) -> int:
        s = set()
        for i in range(len(d)):
            if d[i]% 2 == 0:
                for j in range(len(d)):
                    if j != i:
                        for k in range(len(d)):
                            if k != i and k != j and d[k] != 0:
                                s.add(str(d[k])+ str(d[j])+ str(d[i]))
        return len(s)
