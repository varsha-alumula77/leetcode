class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        i=0
        while i<len(nums):
            left_sum=0
            right_sum=0
            for left in range(i):
                left_sum+=nums[left]
            for right in range(i+1,len(nums)):
                right_sum+=nums[right]
            res.append(abs(left_sum-right_sum))
            i+=1
        return res