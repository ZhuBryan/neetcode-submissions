class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        large = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                large = max(large, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            large = max(large, h * (len(heights) - i))
        return large