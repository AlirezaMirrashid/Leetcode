"""
🔷 LeetCode 129 - Sum Root to Leaf Numbers

🧠 Task:
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number (concatenate node values).
Return the total sum of all root-to-leaf numbers. A leaf is a node with no children.

-----------------------------------
Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
 Paths: 1->2 = 12, 1->3 = 13, sum = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
 Paths: 4->9->5 = 495, 4->9->1 = 491, 4->0 = 40, sum = 495+491+40 = 1026.

-----------------------------------
Constraints:
- Number of nodes in [1,1000].
- Node.val in [0,9].
- Depth <= 10.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        ✅ DFS Preorder Accumulation

        Traverse the tree, carrying the current path value. At each node:
          current_number = prev_number * 10 + node.val
        When reaching a leaf, add current_number to total.

        Time Complexity: O(N) -- visits each node once.
        Space Complexity: O(H) recursion stack, H = tree height (<=10).
        """
        def dfs(node: TreeNode, current: int) -> int:
            if not node:
                return 0
            current = current * 10 + node.val
            # if leaf, return the number formed
            if not node.left and not node.right:
                return current
            # else sum from subtrees
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)

    def sumNumbersBruteForce(self, root: Optional[TreeNode]) -> int:
        """
        ❌ Brute Force: collect all paths then convert

        1. Use DFS to collect each root-to-leaf path as list of digits.
        2. Convert each path to integer and sum.

        Time Complexity: O(N*H) to build paths and convert, H depth.
        Space Complexity: O(N*H) for storing all paths.
        """
        paths = []
        def dfs_collect(node: TreeNode, path: list):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append(int("".join(path)))
            else:
                dfs_collect(node.left, path)
                dfs_collect(node.right, path)
            path.pop()

        dfs_collect(root, [])
        return sum(paths)

# 🔸 Helper to build tree and test

def build_tree(vals):  # level-order list -> TreeNode
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kid_idx = 1
    for i, node in enumerate(nodes):
        if node:
            if kid_idx < len(nodes):
                node.left = nodes[kid_idx]
                kid_idx += 1
            if kid_idx < len(nodes):
                node.right = nodes[kid_idx]
                kid_idx += 1
    return nodes[0]

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    root1 = build_tree([1,2,3])
    print(sol.sumNumbers(root1), "expected 25")
    print(sol.sumNumbersBruteForce(root1), "expected 25")
    # Example 2
    root2 = build_tree([4,9,0,5,1])
    print(sol.sumNumbers(root2), "expected 1026")
    print(sol.sumNumbersBruteForce(root2), "expected 1026")
