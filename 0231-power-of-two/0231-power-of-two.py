class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        res=1
        while res<n:
            if res*2==n:
                return True
            res=res*2
        return False

        