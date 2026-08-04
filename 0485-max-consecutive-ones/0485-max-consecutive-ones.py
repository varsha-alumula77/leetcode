class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con=0
        temp=0
        for i in range(len(nums)):  
            if nums[i]==1:
                temp+=1
            else:
                max_con=max(temp,max_con)
                temp=0
        if nums[-1]==1:
            max_con=max(temp,max_con)
        return max_con

                