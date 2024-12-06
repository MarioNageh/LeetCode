class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban_set = set(banned)
        cur_sum = 0
        count = 0

        
        for i in range(1,n+1):
            if cur_sum >= maxSum or cur_sum + i > maxSum:
                break
            if i in ban_set:
                continue
            cur_sum += i
            count +=1
        return count