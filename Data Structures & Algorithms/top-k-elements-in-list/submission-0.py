class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valmap={}
        buckets=[[] for _ in range(len(nums)+1)]
        for num in nums:
            if num in valmap:
                valmap[num] += 1
            else: 
                valmap[num] = 1
        
        for num in valmap:
            buckets[valmap[num]].append(num)

        result = []
        for i in range (len(nums), -1, -1):
            current_bucket = buckets[i]
            for elem in current_bucket:
                result.append(elem)
                k -= 1
                if k == 0:
                    return result 
        return


