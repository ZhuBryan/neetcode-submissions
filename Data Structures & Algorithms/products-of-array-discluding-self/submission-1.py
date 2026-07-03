class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1 for _ in range(n)]
        left = 1
        for l in range(n):
            output[l] *= left
            left *= nums[l]
        
        right = 1
        for r in range(n-1, -1, -1):
            output[r] *= right
            right *= nums[r]

        return output