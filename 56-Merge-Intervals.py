class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <=0:
            return intervals

        y = sorted(intervals, key=lambda x:x[0])
        res =[]

        for start,end in y:
            last = res[-1] if len(res) >0 else None
            if last and  start <= last[1]:
                res[-1][1] = max(end,res[-1][1])
            else:
                res.append([start,end])
        return res