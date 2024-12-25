# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []
        while q:
            level_size = len(q)
            max_value = float("-inf")

            for _ in range(level_size):
                node = q.popleft()
                max_value = max(max_value,node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(max_value)
        return res

