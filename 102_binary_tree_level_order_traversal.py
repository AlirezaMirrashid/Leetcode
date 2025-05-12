"""
🔷 LeetCode 102 – Binary Tree Level Order Traversal

🧠 Problem Summary:
Given the root of a binary tree, return the level order traversal 
(i.e., left-to-right, level by level) of its nodes' values.

✅ Constraints:
- 0 <= number of nodes <= 2000
- -1000 <= Node.val <= 1000

---

📌 Examples:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

---

💡 Core Idea:
Use a queue (BFS) to traverse the tree level by level and collect values.
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    # Example: build tree [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    sol = Solution()
    print(sol.levelOrder(root))  # [[3],[9,20],[15,7]]

"""
⏱ Time Complexity: O(n)
- Visit every node once

💾 Space Complexity: O(n)
- Queue can hold up to a full level (worst case ~n/2 nodes)
"""
