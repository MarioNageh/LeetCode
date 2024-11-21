from typing import List

def expand(matrix,guard):
    m = len(matrix)
    n = len(matrix[0])
    i = guard[0]
    j = guard[1]
    total_guarded = 0


    # Expand to the left
    left = j - 1
    while left >= 0 and matrix[i][left] != "W" and matrix[i][left] != "G":
        if matrix[i][left] == 0:
            matrix[i][left] = "X"
            total_guarded += 1
        left -= 1

    # Expand to the right
    right = j + 1
    while right < n and matrix[i][right] != "W" and matrix[i][right] != "G":
        if matrix[i][right] == 0:
            matrix[i][right] = "X"
            total_guarded += 1
        right += 1



    # Expand Up

    up = i - 1
    while up >= 0 and matrix[up][j] != "W" and matrix[up][j] != "G":
        if matrix[up][j] == 0:
            matrix[up][j] = "X"
            total_guarded += 1
        up -= 1

    # Expand Down
    down = i + 1
    while down < m and matrix[down][j] != "W" and matrix[down][j] != "G":
        if matrix[down][j] == 0:
            matrix[down][j] = "X"
            total_guarded += 1
        down += 1

    return total_guarded


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        total_unguarded = m * n

        for wall in walls:
            matrix[wall[0]][wall[1]] = "W"
            total_unguarded -= 1


        for guard in guards:
            matrix[guard[0]][guard[1]] = "G"
            total_unguarded -= 1


        for guard in guards:
            total_unguarded -= expand(matrix,guard)

        return total_unguarded
