class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = float('-inf')
        n = len(height)
        i = 0
        j = n-1
        while(i<j):
            area = (j-i)*min(height[i], height[j])
            max_area = max(area, max_area)
            if(height[i] <= height[j]):
                i += 1
            else:
                j -= 1
        return max_area
        