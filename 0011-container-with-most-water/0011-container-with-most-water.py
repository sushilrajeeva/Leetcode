class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left: int = 0
        n: int = len(height)
        right: int = n - 1

        while left < right:
            length: int = min(height[left], height[right])
            breadth: int = right - left
            max_area = max(max_area, length * breadth)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
            

        