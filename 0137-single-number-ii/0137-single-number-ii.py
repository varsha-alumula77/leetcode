class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        for num in nums:
            if d[num]==1:
                return num