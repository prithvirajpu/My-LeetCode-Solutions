class Solution:
    def isValid(self, s: str) -> bool:
        check={'{':'}','[':']','(':')'}
        result=[]
        for i in s:
            if i in check:
                result.append(i)
            else:
                if not result or check[result[-1]]!=i:
                    return False
                result.pop()
        if len(result)!=0:
            return False
        else:
            return True