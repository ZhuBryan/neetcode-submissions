class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = {}
        for l in tasks:
            map[l] = map.get(l, 0) + 1
        heap = [-count for count in map.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque()
        while heap or queue:
            while queue and queue[0][1] <= time:
                freq, _ = queue.popleft()
                heapq.heappush(heap, freq)

            if not heap:
                time = queue[0][1]
                continue
            else:
                time += 1
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    queue.append((freq + 1, time + n))
        
        return time
