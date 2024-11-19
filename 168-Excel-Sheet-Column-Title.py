class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def convertNumberToChar(n):
            return chr(ord(\A\) - 1 + n)
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            char_idx = columnNumber % 26
            res.append(convertNumberToChar(char_idx+1))
            columnNumber //= 26

        return \\.join(reversed(res))