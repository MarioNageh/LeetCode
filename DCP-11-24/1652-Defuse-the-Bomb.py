class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res


        if k > 0:
            res[0] = csum = sum(code[1: k + 1])
            for l in range(1,n):
                r = (l+k)%n
                csum += code[r] - code[l]
                res[l] = csum
            return res
        
        res[0] = csum = sum(code[-1:k-1:-1])
        for l in range(1,n):
            r = (l - k)%n
            csum += code[-r] - code[-l]
            res[-l]=csum
        return res
