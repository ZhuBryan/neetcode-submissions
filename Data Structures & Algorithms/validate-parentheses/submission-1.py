class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for char in s:
            if char in '({[':
                seen.append(char)
            else: 
                if not seen:
                    return False
                top = seen.pop()
                if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                    return False
        return not seen
