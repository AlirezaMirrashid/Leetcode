"""
🔷 LeetCode 270 - Closest Binary Search Tree Value

📘 Problem:
Given the root of a binary search tree (BST) and a target value, return the value in the BST that is closest to the target.

📌 Notes:
- The target value is a floating-point number.
- It is guaranteed that there is exactly one value in the BST that is closest to the target.

🧠 Example:
Input: root = [4,2,5,1,3], target = 3.714286

        4
       / \
      2   5
     / \
    1   3

Output: 4

🔒 Constraints:
- The tree is non-empty.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        ✅ Binary Search-like traversal (Iterative)
        Traverse the BST to find the value closest to the target.

        ⏱ Time Complexity: O(h), where h is the height of the tree (O(log n) if balanced, O(n) worst-case)
        💾 Space Complexity: O(1)
        """
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest

    def closestValueRecursive(self, root: TreeNode, target: float) -> int:
        """
        ✅ Recursive approach
        Compare current node and recurse in the relevant subtree.

        ⏱ Time Complexity: O(h)
        💾 Space Complexity: O(h) due to recursion stack
        """
        def dfs(node: TreeNode, closest: int) -> int:
            if not node:
                return closest
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            if target < node.val:
                return dfs(node.left, closest)
            else:
                return dfs(node.right, closest)
        return dfs(root, root.val)


# 🔸 Example Usage:
if __name__ == "__main__":
    # Manually constructing the BST from the example: [4,2,5,1,3]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    target = 3.714286
    sol = Solution()
    print("Closest (Iterative):", sol.closestValue(root, target))   # Output: 4
    print("Closest (Recursive):", sol.closestValueRecursive(root, target))  # Output: 4

"""
🧠 Complexity Analysis:
- Time Complexity: O(h), where h is the height of the BST.
- Space Complexity:
    - Iterative: O(1)
    - Recursive: O(h) due to call stack
"""

