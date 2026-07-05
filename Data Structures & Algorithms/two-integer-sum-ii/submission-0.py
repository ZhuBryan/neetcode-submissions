class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            add = numbers[p1] + numbers[p2]
            if add == target:
                return [p1 + 1, p2 + 1]
            elif add < target:
                p1 += 1
            else:
                p2 -= 1
        return
