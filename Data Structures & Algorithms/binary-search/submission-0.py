class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        for i in range(len(nums)):
            mid = (right + left) // 2
            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        return -1