class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res=1
        while left<right:
            right=right&right-1
        return right

