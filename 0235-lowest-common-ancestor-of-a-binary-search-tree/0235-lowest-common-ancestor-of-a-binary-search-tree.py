# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        road1 = []
        road2 = set()
        
        curr1 = root
        curr2 = root
        while(curr1):
            road1.append(curr1)
            if curr1.val > p.val:
                curr1 = curr1.left
            elif curr1.val < p.val:
                curr1 = curr1.right
            else:
                break
        
        while(curr2):
            road2.add(curr2)
            if curr2.val > q.val:
                curr2 = curr2.left
            elif curr2.val < q.val:
                curr2 = curr2.right
            else:
                break

        for idx in range(len(road1)-1, -1, -1):
            if road1[idx] in road2:
                return road1[idx]
        