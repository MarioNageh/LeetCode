class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx,val in enumerate(nums):
            complemenrty = target - val
            if complemenrty in res:
                return [res[complemenrty],idx]


            res[val] = idx

