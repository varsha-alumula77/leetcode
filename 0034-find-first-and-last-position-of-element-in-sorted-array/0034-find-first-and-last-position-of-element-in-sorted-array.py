class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        ans1=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans1=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        left=0
        right=len(nums)-1
        ans2=-1
        while left<=right:
            mid1=(left+right)//2
            if nums[mid1]==target:
                ans2=mid1
                right=mid1-1
            elif nums[mid1]>target:
                right=mid1-1
            else:
                left=mid1+1
        return ans2,ans1
