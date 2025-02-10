class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s) # To List Of Strings 
        j = 0
        for idx,c in enumerate(s):
            if c.isdigit() and j > 0:
                j -= 1
            else:
                s[j] = c
                j += 1
        s = s[:j]
        return "".join(s)
        