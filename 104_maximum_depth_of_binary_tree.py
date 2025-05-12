"""
🔷 LeetCode 104 – Maximum Depth of Binary Tree

🧠 Problem Summary:
Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

✅ Constraints:
- The number of nodes is in the range [0, 10⁴].
- -100 <= Node.val <= 100

---

📌 Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

---

💡 Approaches:

1. **DFS Recursion**
   - Recursively compute the depth of left and right subtrees, then take max +1.

2. **BFS (Level Order Traversal)**
   - Use a queue and count levels.

"""

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        """DFS recursive solution."""
        if not root:
            return 0
        left = self.maxDepth_dfs(root.left)
        right = self.maxDepth_dfs(root.right)
        return max(left, right) + 1

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        """BFS level-order solution."""
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    # Example: root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print("DFS:", sol.maxDepth_dfs(root))   # Output: 3
    print("BFS:", sol.maxDepth_bfs(root))   # Output: 3

"""
⏱ Time Complexity:
- DFS: O(n), where n = number of nodes (visit each node once)
- BFS: O(n), visit each node once

💾 Space Complexity:
- DFS: O(h) for call stack, h = tree height (worst case O(n), best case O(log n))
- BFS: O(n) for queue (at worst, when bottom level is full)
"""
