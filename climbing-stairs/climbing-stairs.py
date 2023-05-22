class Solution:
    def climbStairs(self, n: int) -> int:
        fir, sec = 1, 1
        for i in range(n - 1):
            tmp = fir + sec
            fir = sec
            sec = tmp
        
        return sec