\\\
Boyer-Moore Voting
For Finding majority element in o(n) rather that nlog(n) because of sorting
\\\

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count +=1
            else:
                count -=1


        return candidate