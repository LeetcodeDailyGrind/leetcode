# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # define a helper method to help getting the paths to the leave nodes
        # list of the paths of leave nodes
        def dfs(node, path, paths):
            if not node.left and not node.right:
                paths.append(list(path))
                return

            if node.left:
                path.append('L')
                dfs(node.left, path, paths)
                path.pop()
            if node.right:
                path.append('R')
                dfs(node.right, path, paths)
                path.pop()
        
        paths = []
        dfs(root, [], paths)
        result = 0
        n = len(paths)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                prefix_length = 0
                for k in range(min(len(paths[i]), len(paths[j]))):
                    if paths[i][k] != paths[j][k]:
                        break
                    prefix_length += 1

                if len(paths[i]) + len(paths[j]) - 2 * prefix_length <= distance:
                    result += 1

        return result