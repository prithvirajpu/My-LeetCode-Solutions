class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l=0
        r=len(height)-1
        while l<r:
            mini_height=min(height[l],height[r])
            width=r-l
            answer=mini_height*width
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
            max_area=max(max_area,answer)
        return max_area