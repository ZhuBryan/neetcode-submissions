class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sub = []
        for i in range (0, len(nums)):
            if nums[i] in sub:
                return True
            else: 
                sub.append(nums[i])
        return False