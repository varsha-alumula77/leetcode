class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        for j in nums:
            if d[j]==1:
                return j