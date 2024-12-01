class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res = {}
        for idx,n in enumerate(arr):
            if (n * 2) in res or ((n // 2) in res and n%2==0):
                return True
            res[n] = idx
        return False
            

        