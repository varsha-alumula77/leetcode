class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low=0
        # high=len(nums)-1
        # ans=float(inf)
        # while low<=high:
        #     mid=(low+high)//2
        #     if nums[low]<nums[mid]:
        #         if nums[low]<ans:
        #             ans=nums[low]
        #         low=mid+1
        #     else:
        #         if nums[mid]<ans:
        #             ans=nums[mid]
        #         high=mid-1
        # return ans

        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]

        