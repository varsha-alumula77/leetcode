class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            temp=[]
            while num>0:
                last_digit=num%10
                temp.insert(0,last_digit)
                num=num//10
            res.extend(temp)
        return res 
        