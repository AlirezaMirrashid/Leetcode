"""
🔷 LeetCode 543 - Diameter of Binary Tree

🧠 Task:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter is the length (number of edges) of the longest path between any two nodes. The path may or may not pass through the root.

-----------------------------------
Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: The path [4,2,1,3] or [5,2,1,3] has length 3.

Example 2:
Input: root = [1,2]
Output: 1

-----------------------------------
Constraints:
- The number of nodes is in [1, 10^4].
- -100 <= Node.val <= 100
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        ✅ Optimal DFS Approach (Single pass)

        Compute the height of each subtree via DFS, and at each node the local diameter is
        left_height + right_height. Track the maximum across all nodes.

        Time Complexity: O(n) -- each node visited once.
        Space Complexity: O(h) recursion stack, where h is tree height.
        """
        self.ans = 0
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            # update diameter: edges = lh + rh
            self.ans = max(self.ans, lh + rh)
            # return height in edges
            return max(lh, rh) + 1

        height(root)
        return self.ans

    def diameterOfBinaryTreeBruteForce(self, root: Optional[TreeNode]) -> int:
        """
        ❌ Brute Force Approach (O(n^2))

        For each node, compute its height repeatedly and combine every pair of nodes to find
        longest path passing through their lowest common ancestor.
        Here we simplify by computing for each node the sum of heights of left and right subtrees,
        but recompute heights from scratch at each node.

        Time Complexity: O(n^2) in worst case (skewed tree).
        Space Complexity: O(n) recursion stack.
        """
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(height(node.left), height(node.right)) + 1

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # diameter passing through this node
            d = height(node.left) + height(node.right)
            # best in subtrees
            return max(d, dfs(node.left), dfs(node.right))

        return dfs(root)

# 🔸 Helper to build tree from list (level-order)
def build_tree(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# 🔸 Sample tests
if __name__ == '__main__':
    sol = Solution()
    tests = [
        ([1,2,3,4,5], 3),
        ([1,2], 1),
        ([1,2,3,4,None,None,5], 3)
    ]
    for vals, expected in tests:
        root = build_tree(vals)
        out = sol.diameterOfBinaryTree(root)
        out_b = sol.diameterOfBinaryTreeBruteForce(root)
        print(f"Tree: {vals} -> Optimal: {out}, Brute: {out_b}, Expected: {expected}")
