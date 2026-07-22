class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=n*(n+1)
        b=n*n
        while b!=0:
            a,b=b,a%b
        return a

