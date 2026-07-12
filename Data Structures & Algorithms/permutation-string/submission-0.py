class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_sub = [0 for _ in range(26)]
        count = [0 for _ in range(26)]
        for i in s1:
            count_sub[ord(i) - ord('a')] += 1
        for r in range (len(s2)):
            count[ord(s2[r]) - ord('a')] += 1
            
            if r >= len(s1):
                count[ord(s2[r - len(s1)]) - ord('a')] -= 1
            if count == count_sub:
                return True
        return False