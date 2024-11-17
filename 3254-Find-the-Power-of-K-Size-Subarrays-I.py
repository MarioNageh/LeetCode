from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = 0
        n = len(nums)
        res = []
        count = 1
        for r in range(n):
            if r>0 and nums[r - 1] + 1 == nums[r]:
                count += 1

            window = r - l + 1
            if window > k:
                if nums[l] + 1 == nums[l + 1]:
                    count -= 1
                l += 1

            window = r - l + 1
            if window == k:
                if count == k:
                    res.append(nums[r])
                else:
                    res.append(-1)


        return res

