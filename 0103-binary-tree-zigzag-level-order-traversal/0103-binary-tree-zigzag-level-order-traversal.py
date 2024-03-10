from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if root is None:
            return results
        
        queue = deque()
        queue.append(root)
        leftToRight = True
        
        while queue:
            currentLevel = deque()
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
               
            results.append(currentLevel)
            leftToRight = not leftToRight
        return results
            
                
        