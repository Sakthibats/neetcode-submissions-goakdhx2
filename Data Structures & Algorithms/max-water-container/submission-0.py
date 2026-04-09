class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx = 0
        right = len(heights)-1
        left = 0
        while right>left:
            lh, rh = heights[left], heights[right]
            maxx = max(min(lh, rh) * (right-left) , maxx)
            if rh>lh:
                left+=1
            else:
                right-=1
        return maxx

        