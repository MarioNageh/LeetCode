class Solution:
    def continuousSubarrays(self, nums):
        from collections import deque
        
        left = 0
        result = 0
        maxDeque = deque()
        minDeque = deque()

        for right , num in enumerate(nums):
            # maxDeque: Maintain decreasing order
            while maxDeque and nums[maxDeque[-1]] <= num:
                maxDeque.pop()
            maxDeque.append(right)

            # minDeque: Maintain increasing order
            while minDeque and nums[minDeque[-1]] >= num:
                minDeque.pop()
            minDeque.append(right)

            # Ensure the window is valid
            while nums[maxDeque[0]] - nums[minDeque[0]] > 2:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()

            result += right - left + 1

        return result
