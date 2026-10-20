class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        res=[]
        for i in range(mini,maxi):
            if i not in nums:
                res.append(i)
        return res if res else []