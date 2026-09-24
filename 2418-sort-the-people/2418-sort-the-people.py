class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        res=[]
        result={}
        for i in range(len(heights)):
            result[heights[i]]=names[i]
        heights.sort()
        for i in reversed(heights):
            # print(res)
            res.append(result[i])
        return res