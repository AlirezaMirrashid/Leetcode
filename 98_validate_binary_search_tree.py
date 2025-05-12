"""
🔷 LeetCode 98 - Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

Rules for BST:
1. Left subtree nodes must be < current node.
2. Right subtree nodes must be > current node.
3. Both left and right must themselves be valid BSTs.

-----------------------------------------------------------
Example 1:
Input: root = [2,1,3]
Output: True
Explanation: Left child 1 < 2, right child 3 > 2, both subtrees valid.

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: False
Explanation: 4 is in the right subtree of 5 but 4 < 5. Invalid.

Constraints:
- 1 <= nodes <= 10^4
- Node values are between -2^31 and 2^31-1
-----------------------------------------------------------
"""

from typing import Optional

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST_DFSBounds(self, root: Optional[TreeNode]) -> bool:
        """
        ✅ Recursive DFS with lower and upper bounds.
        """

        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root)

    def isValidBST_InorderTraversal(self, root: Optional[TreeNode]) -> bool:
        """
        ✅ Inorder traversal should produce a strictly increasing list.
        """

        self.prev = None

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)

        return inorder(root)

    def isValidBST_BruteForce(self, root: Optional[TreeNode]) -> bool:
        """
        🚫 Brute force (not optimal): For each node, check all left subtree < node and right subtree > node.
        (Not recommended, O(n²) worst-case.)
        """

        def is_less_than(node, val):
            if not node:
                return True
            if node.val >= val:
                return False
            return is_less_than(node.left, val) and is_less_than(node.right, val)

        def is_greater_than(node, val):
            if not node:
                return True
            if node.val <= val:
                return False
            return is_greater_than(node.left, val) and is_greater_than(node.right, val)

        if not root:
            return True

        if not is_less_than(root.left, root.val) or not is_greater_than(root.right, root.val):
            return False

        return self.isValidBST_BruteForce(root.left) and self.isValidBST_BruteForce(root.right)


# 🔸 Sample usage
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST_DFSBounds(root))  # True
    print(sol.isValidBST_InorderTraversal(root))  # True

    # Example 2
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(sol.isValidBST_DFSBounds(root))  # False
    print(sol.isValidBST_InorderTraversal(root))  # False

# -----------------------------------------------------------
# ✅ Time Complexity:
# DFS Bounds: O(n) - Visit each node once.
# Inorder: O(n) - Visit each node once.
# Brute Force: O(n²) - Every node may traverse subtrees.

# ✅ Space Complexity:
# O(h) - where h = height of tree (due to recursion stack)
# Worst case h = n for skewed tree; average case h = log n for balanced tree.

