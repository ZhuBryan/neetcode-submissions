class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for n in word:
                ind = ord(n) - ord('a')
                letters[ind] += 1
            key = tuple(letters)
            group[key].append(word)
        return list(group.values())

