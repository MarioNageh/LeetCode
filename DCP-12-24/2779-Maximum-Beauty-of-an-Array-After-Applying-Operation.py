class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        # find the maxSub Array A[i..j] such A[j] - A[i] <= 2k
        l = 0
        for r in range(len(nums)):
            
            while nums[r] - nums[l] > 2*k:
                l += 1
            
            win_len = r - l + 1
            res = max(res , win_len)

        return res