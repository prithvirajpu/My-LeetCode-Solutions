class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count += 1
                  
        # while 0 in nums:
        #     nums.remove(0)

        # for i in range(count):
        #     nums.append(0)                            
                    
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        