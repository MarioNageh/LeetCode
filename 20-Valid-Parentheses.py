class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in mapping:
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0