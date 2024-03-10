from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        if root is None:
            return results

        queue = deque()
        queue.append(root)

        while queue:
            levelSum = len(queue)
            currentLevel = []

            for i in range(levelSum):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

            results.append(currentLevel[-1]) 

        return results