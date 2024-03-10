from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        results = []
        if root is None:
            return results
        
        queue = deque()
        queue.append(root)
        
        while queue:
            levelSum = 0.0
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                levelSum += currentNode.val
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            results.append(levelSum / levelSize)
        return results
        
        
            
        