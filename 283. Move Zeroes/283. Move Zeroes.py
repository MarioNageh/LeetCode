class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z] = nums[i]
                z += 1
        for i in range(z, len(nums)):
            nums[i] = 0
