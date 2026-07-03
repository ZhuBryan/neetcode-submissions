class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets = {}
        sett = {}
        for e in s:
            if e in sets:
                sets[e] += 1
            else:
                sets[e] = 1
        for e in t:
            if e in sett:
                sett[e] += 1
            else:
                sett[e] = 1

        return sets == sett