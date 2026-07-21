class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        large = 0
        stack = []
        for n in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[n]:
                height = heights[stack.pop()]
                right = n
                left = stack[-1] if stack else -1
                large = max(large, (right - left - 1) * height)
            stack.append(n)
        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            right = len(heights)
            large = max(large, (right - left - 1) * height)
        return large