class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        bucket = 0
        minwall = 0
        while left<right:
            hl, hr = height[left], height[right]
            minwall = max(minwall, min(hl, hr))
            if hl>hr:
                bucket+= max(0, minwall-hr)
                right-=1
            else:
                bucket+= max(0, minwall-hl)
                left+=1
        return bucket


        
        