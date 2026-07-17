class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        i=0
        res=[]
        while i<len(nums):
            left_ele=set()
            right_ele=set()
            for j in range(i+1):
                left_ele.add(nums[j])
            for k in range(i+1,len(nums)):
                right_ele.add(nums[k])
            res.append(len(left_ele)-len(right_ele))
            i+=1
        return res


