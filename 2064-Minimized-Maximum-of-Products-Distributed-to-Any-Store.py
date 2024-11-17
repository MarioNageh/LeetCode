class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x):
            stores = 0
            for i in quantities:
                stores += math.ceil(i / x)
            return stores <= n
        
        
        l ,r = 1 , max(quantities)
        res = 0
        while r >= l:
            m = (l + (r - l) // 2)
            if can_distribute(m):
               res = m
               r = m - 1
            else:
                l = m + 1
        return res
        