class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            left_ele=[]
            right_ele=[]
            for j in range(i+1):
                if nums[j] not in left_ele:
                    left_ele.append(nums[j])
            for k in range(i+1,len(nums)):
                if nums[k] not in right_ele:
                    right_ele.append(nums[k])
            temp=len(left_ele)-len(right_ele)
            res.append(temp)
            i+=1
        return res


