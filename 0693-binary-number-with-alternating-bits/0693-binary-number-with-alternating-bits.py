class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # temp=-1
        # while n>0:
        #     if n%2==temp:
        #         return False
        #     temp=n%2
        #     n=n//2
        # return True
        lis=[]
        while n>0:
            lis.append(n%2)
            n=n//2
        for i in range(1,len(lis)):
            if lis[i-1]==lis[i]:
                return False
        return True

        