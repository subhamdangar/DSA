class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        c = 0
        for i in range(0, n+1):
            a = b
            b = c
            c = a + b

        return c

        