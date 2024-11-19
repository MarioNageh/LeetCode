class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l = 0
        cur_sum = 0
        res = 0
        prev_idx = {}
        for r in range(n):
            cur_sum += nums[r]
            i = prev_idx.get(nums[r], -1)

            while l <= i or r - l + 1 > k:
                cur_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = max(res, cur_sum)

            prev_idx[nums[r]] = r
        return res