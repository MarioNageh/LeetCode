from bisect import bisect_right
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        max_weights = [0]
        max_weight_ends = [-1]

        events.sort(key = lambda x: x[1])

        max_two = 0
        for start, end, weight in events:
            index = bisect_right(max_weight_ends, start - 1) - 1
            
            if weight + max_weights[index] > max_two:
                max_two = weight + max_weights[index]
            if weight > max_weights[-1]:
                max_weights.append(weight)
                max_weight_ends.append(end)
        
        return max_two
