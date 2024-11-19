class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        l, idx, h = 0, 0, len(nums) - 1
        #it's so similar to move zeros to left
        while idx <= h:
            if nums[idx] == 0:
                nums[idx],nums[l] = nums[l],nums[idx]
                l += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx],nums[h] = nums[h],nums[idx]
                h -= 1
            else:
                idx += 1
            
