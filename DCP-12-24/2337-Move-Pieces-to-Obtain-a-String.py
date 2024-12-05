class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i , j = 0 , 0
        window_idx = -1

        def skip(s,n,idx):
            while idx < n and s[idx] == "_":
                idx +=1
            return idx

        while i < n:
            i = skip(start,n,i)
            j = skip(target,n,j)

            if i == n and j == n:
                return True

            if i==n or j==n or start[i] != target[j]:
                return False
            
            if start[i] == 'L' and (j <= window_idx or j > i):
                return False
            elif start[i] == 'R' and (i > j):
                return False
            window_idx = j
            i += 1
            j += 1
        
        i = skip(start,n,i)
        j = skip(target,n,j)
        return i == n and j ==n