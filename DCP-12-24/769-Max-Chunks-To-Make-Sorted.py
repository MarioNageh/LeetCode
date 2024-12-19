class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        res = 0
        cur_max = -1
        for idx , val in enumerate(arr):
            cur_max = max(cur_max , val)

            if cur_max == idx:
                res += 1

        return res

        