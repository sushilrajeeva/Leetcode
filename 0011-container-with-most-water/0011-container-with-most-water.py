class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area: int = 0
        left: int = 0
        n: int = len(height)
        right: int = n-1

        while left < right:
            width: int = right - left
            length: int = min(height[left], height[right])
            a: int = width * length
            area = max(a, area)
            if height[left] < height[right]:
                left += 1
            else: right -= 1

        return area
