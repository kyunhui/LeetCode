# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node):
        if node.left or node.right:
            return False
        else:
            return True
        
    def sumStack(self, stack):
        depth = len(stack)-1
        sum = 0
        
        for i in stack:
            sum += i.val * 10**depth
            depth -= 1
            
        return sum 
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        answer = 0
        stack = [root]
        current = root 
        
        while True:
            
            while not(self.isLeaf(current)):
                if not(current.left):
                    tmp = current.right
                    current.right = None
                else:
                    tmp = current.left
                    current.left = None
                    
                current = tmp 
                stack.append(current)
            
            
            answer += self.sumStack(stack)
            
            while self.isLeaf(current):
                
                if not(len(stack)):
                    return answer
                
                current = stack.pop()
                
            stack.append(current)
                  
                