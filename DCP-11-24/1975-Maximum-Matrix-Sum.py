class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        neg_count = 0
        min_element = float('inf')
        for row in matrix:
            for col in row:
                res += abs(col)
                min_element = min(min_element,abs(col))
                neg_count += 1 if col < 0 else 0
        if neg_count & 1:
            res -= 2 * min_element

        return res