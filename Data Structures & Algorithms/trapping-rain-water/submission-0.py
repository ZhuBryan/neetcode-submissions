class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        top = 0
        for i in range(len(height)):
            top = max(height[i], top)
            left[i] = top
        top = 0
        for j in range(len(height) - 1, -1, -1):
            top = max(height[j], top)
            right[j] = top
        
        sum = 0
        for k in range(len(height)):
            sum += min(left[k], right[k]) - height[k]

        return sum