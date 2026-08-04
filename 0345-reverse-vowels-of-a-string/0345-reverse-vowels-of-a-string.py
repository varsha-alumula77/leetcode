class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels='aeiouAEIOU'
        # l=0
        # r=len(s)-1
        # while l<r:
        #     if s[l] in vowels and s[r] in vowels:
        #         s[l],s[r]=s[r],s[l]
        #         l+=1
        #         r-=1
        #     elif s[l] not in vowels:
        #         l+=1
        #     else:
        #         r-=1
        # res="".join(s)
        # return res

        left=0
        right=len(s)-1
        while left<right:
            while left <right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return "".join(s)



