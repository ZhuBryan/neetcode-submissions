class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + "#" + s
        return new_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0;
        j = 0;
        while i < len(s):
            if s[j] != "#":
                j += 1
            else:
                length = int(s[i:j])
                strs.append(s[j+1:(j+length+1)])
                i = j + length + 1
                j = i
        return strs

            
