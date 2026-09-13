class Solution:
    def helper(self,m):
        l = len(m)
        nsr = [l]*l
        nsl = [-1]*l
        s1 = []
        s2 = []
        for i in range(l):
            while s1 and m[i] <= m[s1[-1]]:
                s1.pop()
            if s1:
                nsl[i] = s1[-1]
            s1.append(i)
        for i in range(l-1,-1,-1):
            while s2 and m[i] <= m[s2[-1]]:
                s2.pop()
            if s2:
                nsr[i] = s2[-1]
            s2.append(i)
        ans = 0
        for i in range(l):
            height = m[i]
            width = nsr[i] - nsl[i]-1
            ans = max(ans , height *width)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        
        mat = [ [0] * len(matrix[0]) for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    mat[0][j] = (int(matrix[0][j]))
                else:
                    if matrix[i][j] == "0":
                        mat[i][j] = 0
                    elif matrix[i][j] == "1":
                        mat[i][j] = (1 + mat[i-1][j])
        m = 0
        for i in range(len(mat)):
            m = max(m , self.helper(mat[i]))
        return m