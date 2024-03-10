# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        results = 0
        
        if root is None:
            return results
        
        queue = deque()
        queue.append(root)
        minimumTreeDepth = 0
        
        while queue:
            minimumTreeDepth += 1
            levelSize = len(queue)
            
            for _ in range(levelSize):
                currentNode = queue.popleft()
                
                if not currentNode.left and not currentNode.right:
                    return minimumTreeDepth
                
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            results = minimumTreeDepth
        return results