class Solution:
        def minWindow(self, s: str, t: str) -> str:
            def get_idx(ch):
                if 'A' <= ch <= 'Z':
                    return ord(ch) - ord('A') + 26
                else:
                    return ord(ch) - ord('a')
            base = 52 * [0]
            out = 52 * [0]
            for i in range(len(t)):
                base[get_idx(t[i])] += 1

            formed = 0
            l = 0
            length = len(s) + 1
            ans = ""
            required = len(set(t))
            for r in range(len(s)):
                idx = get_idx(s[r])
                out[idx] += 1
                if base[idx] > 0 and base[idx] == out[idx]:
                    formed += 1

                while formed == required and l <= r:
                    if r - l + 1 < length:
                        ans = s[l:r + 1]
                        length = r - l + 1
                    out[get_idx(s[l])] -= 1
                    if base[get_idx(s[l])] > 0 and out[get_idx(s[l])] < base[get_idx(s[l])]:
                        formed -= 1
                    l += 1
            return ans


