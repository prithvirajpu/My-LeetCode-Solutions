class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        new=''
        for i in s.lower():
            # if i.isalpha() or i.isdigit():
            if i.isalnum():
                new+=i
        return new[::-1]==new