class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        top_count = 0
        curr_count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            curr_count = r - l + 1
            top_count = max(top_count, curr_count)
        return top_count
            
            