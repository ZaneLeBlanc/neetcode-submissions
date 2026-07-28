class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        if n == 0:
            return 1

        for a in range(abs(n)-1):
            res = res * x

        if n < 0:
            res = 1/res

        return res

        