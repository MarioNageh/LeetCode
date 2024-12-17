class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = []
        count = Counter(s)
        max_heap = [(-ord(c), cnt) for c, cnt in count.items()]
        heapq.heapify(max_heap)
        while max_heap:
            c , cnt = heapq.heappop(max_heap)
            cur_cnt = min(cnt , repeatLimit)
            remain_char = cnt - cur_cnt
            char = chr(-c)
            res.append(cur_cnt * char)

            if max_heap and remain_char > 0:
                nxt_c , nxt_cnt = heapq.heappop(max_heap)
                char = chr(-nxt_c)
                res.append(char)
                if nxt_cnt > 1:
                    heapq.heappush(max_heap,(nxt_c, nxt_cnt - 1))

                heapq.heappush(max_heap, (c, remain_char))

        return "".join(res)