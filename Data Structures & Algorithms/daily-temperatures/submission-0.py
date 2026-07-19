class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen = []
        i = 0
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while seen and temperatures[i] > temperatures[seen[-1]]:
                past_ind = seen.pop()
                result[past_ind] = i - past_ind
            seen.append(i)
            
        return result