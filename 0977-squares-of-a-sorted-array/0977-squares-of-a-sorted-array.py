class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # res=[]
        # for i in range(len(nums)):
        #     res.append(nums[i]*nums[i])
        # res=sorted(res)
        # return res

        l=0
        r=len(nums)-1
        k=len(nums)-1
        res=[0]*len(nums)
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[k]=nums[l]*nums[l]
                k=k-1
                l=l+1
            else:
                res[k]=nums[r]*nums[r]
                k=k-1
                r=r-1
        return res


