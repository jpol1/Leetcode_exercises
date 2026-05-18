# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res
        queue = [root]
        while queue:
            lq = len(queue)
            level = []
            for idx in range(lq):
                if queue[idx] == None:
                    continue
                level.append(queue[idx].val)
                if (queue[idx].left):
                    queue.append(queue[idx].left)
                if (queue[idx].right):
                    queue.append(queue[idx].right)
            res.append(level)
            queue = queue[lq:]
        return res