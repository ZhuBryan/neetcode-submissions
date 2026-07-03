class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sub = {}
        for num in nums:
            if num in sub:
                return True
            sub[num] = 1
        return False