from heapq import heappush, heappop
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        pass
        mark_index = set()
        min_heap = []
        for idx,val in enumerate(nums):
            heappush(min_heap, (val, idx))

        total_sum = 0
        while min_heap:
            val, idx = heappop(min_heap)
            if idx in mark_index:
                continue

            total_sum += val
            mark_index.add(idx)
            mark_index.add(idx + 1)
            mark_index.add(idx - 1)
        return total_sum