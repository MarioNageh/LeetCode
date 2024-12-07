class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        l = -1
        while r >= 0:
            if s[r] == ' ' and l != -1:
                break
            
            if s[r] != ' ':
                if l == -1:
                    l = r

            r -= 1
        return l - r    