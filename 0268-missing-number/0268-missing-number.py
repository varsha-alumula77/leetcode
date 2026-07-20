class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)+1):
            res=res^i
        for j in range(len(nums)) :
            res=res^nums[j]
        return res