# Leetcode probelem number 11 Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        area = 0
        while low != high:
            area = max(area , min(height[low],height[high]) * (high-low))
            if height[low] > height[high]:
                high -= 1
            else:
                low += 1
                
        return area
