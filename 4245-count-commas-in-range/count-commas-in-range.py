class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        elif n<= 100000:
            return n-999 
        