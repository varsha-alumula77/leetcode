class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x=str(x)
        # l=0
        # r=len(x)-1
        # while l<=r:
        #     if x[l]!=x[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        
        temp=x
        rev=0
        while x>0:
            rev=rev*10+x%10
            x=x//10
        if temp==rev:
            return True
        return False