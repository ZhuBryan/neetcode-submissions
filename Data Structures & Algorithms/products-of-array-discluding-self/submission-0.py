class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else: 
                output.append(nums[i-1]*output[i-1])
        for j in range(len(nums) - 2, -1, -1):
            for k in range(len(nums)-1, j, -1):
                output[j] = output[j] * nums[k]

        return output
        