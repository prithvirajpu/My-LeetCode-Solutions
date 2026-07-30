class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # new={}
        # for i in nums:
        #     if i in new:
        #         new[i]+=1
        #     else:
        #         new[i]=1
        # for i,j in new.items():
        #     if j ==1:
        #         return i
        new=[]
        for i in nums:
            if i in new:
                new.remove(i)
            else:
                new.append(i)
        return new[0]