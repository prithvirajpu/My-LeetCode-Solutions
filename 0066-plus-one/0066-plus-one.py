class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # new="".join(str(i) for i in digits)
        # n=int(new)+1
        # result=[int(i) for i in str(n)]
        # return result
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits