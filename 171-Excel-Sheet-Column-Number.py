class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # char = columnTitle[0]
        # print(ord(char) - ord(\A\) + 1)
        def convert_char_to_number(i , char):
            return (ord(char) - ord(\A\) + 1) * (26 ** i)

        res = 0
        for idx, char in enumerate(reversed(columnTitle)):
            res += convert_char_to_number(idx,char)
        return res