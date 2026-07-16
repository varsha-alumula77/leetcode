class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            total=abs(sum(nums[:i]) - sum(nums[i+1:]))
            res.append(total)
        return res