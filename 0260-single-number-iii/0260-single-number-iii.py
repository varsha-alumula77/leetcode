class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        res=[]
        for key in d:
            if d[key]==1:
                res.append(key)
        return res