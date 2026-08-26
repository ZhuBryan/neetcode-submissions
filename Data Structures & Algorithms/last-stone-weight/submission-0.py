class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        x = 0
        y = 0
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, -(y-x))
        if stones:
            return -heapq.heappop(stones)
        else:
            return 0