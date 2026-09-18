class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palindrome(s):
            if len(s)<2:
                return s
            left=0
            right=len(s)-1
            while left<right:
                if s[left]!=s[right]:
                    return ''
                left+=1
                right-=1
            return s
        for i in words:
            res=palindrome(i)
            if res:
                return res
        return ''