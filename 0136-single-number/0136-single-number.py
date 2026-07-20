class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for val in nums:
            d[val]=d.get(val,0)+1
        for key,value in d.items():
            if value==1:
                return key