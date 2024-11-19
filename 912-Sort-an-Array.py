def merge(left, right, arr):
    idx_l ,idx_r ,idx = 0,0,0
    rn ,rl = len(right),len(left) 
    while idx_l < rl and idx_r < rn:
        if left[idx_l] < right[idx_r]:
            arr[idx] = left[idx_l]
            idx_l += 1
        else:
            arr[idx] = right[idx_r]
            idx_r += 1
        idx += 1

    while idx_l < rl:
        arr[idx] = left[idx_l]
        idx_l += 1
        idx += 1

    while idx_r < rn:
        arr[idx] = right[idx_r]
        idx_r += 1
        idx += 1


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge(left,right,arr)
    return arr


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)