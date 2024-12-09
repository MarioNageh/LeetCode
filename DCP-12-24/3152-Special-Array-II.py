class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        alter_sum = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] & 1 != nums[i - 1] & 1:
                alter_sum[i] = alter_sum[i - 1] + 1

        res = []
        for start, end in queries:
            size = end - start + 1
            res.append(alter_sum[end] >= size)
        return res