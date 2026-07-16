class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=0
        left=0
        for i in nums:
            total+=i
        for i in range(len(nums)):
            if left==(total - left - nums[i]):
                return i
            left+=nums[i]
        return -1
        