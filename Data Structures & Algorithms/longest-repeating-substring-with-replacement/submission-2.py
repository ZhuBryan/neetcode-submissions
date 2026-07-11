class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mydict={}
        best = 0
        freq = 0

        for r in range(len(s)):
            mydict[s[r]] = mydict.get(s[r],0) + 1
            freq = max(mydict[s[r]], freq)
            if ((r-l+1) - freq > k):
                mydict[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
            