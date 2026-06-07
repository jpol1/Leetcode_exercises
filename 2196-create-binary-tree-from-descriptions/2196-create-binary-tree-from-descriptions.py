# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes_dct = {}
        prohibited = set()
        for parent, child, isLeft in descriptions:
            prohibited.add(child)
            
            if parent not in nodes_dct:
                nodes_dct[parent] = TreeNode(parent)
            if child not in nodes_dct:
                nodes_dct[child] = TreeNode(child)
            
            if isLeft:
                nodes_dct[parent].left = nodes_dct[child]
            else:
                nodes_dct[parent].right = nodes_dct[child]

        root = set(nodes_dct.keys()).difference(prohibited).pop()
        return nodes_dct[root]