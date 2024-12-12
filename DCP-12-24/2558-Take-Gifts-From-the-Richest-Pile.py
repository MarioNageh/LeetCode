import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        total_value = sum(gifts)

        for _ in range(k):
            largest_gift = -heapq.heappop(max_heap)
            val = int(largest_gift ** .5)
            total_value = total_value - largest_gift + val
            heapq.heappush(max_heap, -val)
        return total_value