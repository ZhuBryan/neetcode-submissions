from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)
        small = 1
        best = 0
        while small <= top:
            time = 0
            mid = (top + small) // 2
            for n in piles:
                time += ceil(n / mid)
            if time > h:
                small = mid + 1
            elif time <= h:
                best = mid
                top = mid - 1
        return best