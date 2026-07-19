class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        res=1
        while res<n:
            if res*4==n:
                return True
            res=res*4
        return False