class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = {nums[i] for i in range(len(nums))}
        long = 0
        curr = 0
        less = 0
        for num in nums:
            if num - 1 not in lookup:
                curr = 1
                less = num
                for n in nums:
                    if less + 1 in lookup:
                        curr += 1
                        less = less + 1
                    else: 
                        long = max(long, curr)
                        break
        return long