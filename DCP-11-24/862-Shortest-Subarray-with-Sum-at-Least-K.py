class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        cur_sum = 0
        q = deque()
        for idx,val in enumerate(nums):
            cur_sum += val

            if cur_sum >= k:
                res = min(res, idx + 1)
            
            # find min valid window 

            while q and cur_sum - q[0][0] >= k:
                prefix,end_idx = q.popleft()
                res = min(res, idx-end_idx)


            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum,idx))


        return -1 if res == float("inf") else res

        