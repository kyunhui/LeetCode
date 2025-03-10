# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, [])

    def dfs(self, node: TreeNode | None, answer: list[int]) -> list[int]:
        if node == None:
            return answer 
        
        self.dfs(node.left, answer)
        answer.append(node.val)
        self.dfs(node.right, answer)
        
        return answer 