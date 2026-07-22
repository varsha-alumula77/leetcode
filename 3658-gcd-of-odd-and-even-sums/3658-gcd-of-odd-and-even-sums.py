class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # a=n*(n+1)
        # b=n*n
        # while b!=0:
        #     a,b=b,a%b
        # return a
        even=0
        odd=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                even+=i
            else:
                odd+=i
        while odd!=0:
            even,odd=odd,even%odd
        return even

