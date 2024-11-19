class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        idx_l,idx_r,idx=m - 1,n-1,m+n-1

        while idx_l >= 0 and idx_r>= 0:
            if nums1[idx_l] > nums2[idx_r]:
                nums1[idx] = nums1[idx_l]
                idx_l -= 1
            else:
                nums1[idx] = nums2[idx_r]
                idx_r -= 1
            idx -= 1
        
        while idx_l >= 0:
            nums1[idx] = nums1[idx_l]
            idx_l -= 1
            idx -= 1
        
        while idx_r >= 0:
            nums1[idx] = nums2[idx_r]
            idx_r -= 1
            idx -= 1