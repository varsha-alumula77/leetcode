class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=float('inf')
        maxi=float('-inf')
        for i in nums:
            if i<mini:
                mini=i
            if i>maxi:
                maxi=i
        while maxi!=0:
            mini,maxi=maxi,mini%maxi
        return mini
        
        