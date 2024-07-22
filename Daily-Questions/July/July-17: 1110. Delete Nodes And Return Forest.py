# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        to_delete_set = set(to_delete)
        forest = []
        nodes = deque([root])
        #  print(nodes)
        while nodes:
            current_node = nodes.popleft()

            if current_node.left:
                nodes.append(current_node.left)
                if current_node.left.val in to_delete_set:
                    current_node.left = None
            if current_node.right:
                nodes.append(current_node.right)
                if current_node.right.val in to_delete_set:
                    current_node.right = None
            if current_node.val in to_delete_set:
                if current_node.left:
                    forest.append(current_node.left)
                if current_node.right:
                    forest.append(current_node.right)
        
        if root.val not in to_delete_set:
            forest.append(root)

        return forest