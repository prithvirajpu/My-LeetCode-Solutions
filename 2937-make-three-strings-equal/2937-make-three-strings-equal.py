class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n=min(len(s1),len(s2))
        n=min(len(s3),n)
        count=0
        for i in range(n):
            if s1[i]==s2[i] and s2[i]==s3[i]:
                count+=1
            else:
                break
        if count:
            ot=(len(s1)-count)+(len(s2)-count)+(len(s3)-count)
            return ot
        else:
            return -1