class Solution:
    def hammingWeight(self, n: int) -> int:
        temp=0
        while n>0:
            if n%2==1:
                temp+=1
            n=n//2
        return temp
        