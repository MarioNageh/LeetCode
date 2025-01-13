from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for x in count.values():
            if x % 2 == 0:
                res += 2
            else:
                res +=1 
        return res
            