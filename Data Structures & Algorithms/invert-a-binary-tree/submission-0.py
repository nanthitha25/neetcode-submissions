class Solution:
    def invertTree(self, root):

        # Base Case
        if root is None:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root