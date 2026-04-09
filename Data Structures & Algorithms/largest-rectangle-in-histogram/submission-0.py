class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        for i in range(len(heights)):
            minheight = heights[i]
            for j in range(i, len(heights)):
                minheight = min(minheight, heights[j])
                maxx = max(maxx, (j-i+1)*minheight)
        return maxx
        