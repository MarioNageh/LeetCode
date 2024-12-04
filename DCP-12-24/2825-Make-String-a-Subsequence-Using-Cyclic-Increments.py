class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False


        next_char_map = {chr(i): chr((i - ord('a') + 1) % 26 + ord('a')) for i in range(ord('a'), ord('z') + 1)}
        
        i, j = 0, 0
        while i < len(str1) and j < len(str2):


            if str1[i] == str2[j] or next_char_map[str1[i]] == str2[j]:
                j += 1
                if j == len(str2): 
                    return True
            i += 1
        
        return j == len(str2)