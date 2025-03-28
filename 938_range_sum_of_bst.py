# LeetCode 938: Range Sum of BST
# Problem Link: https://leetcode.com/problems/range-sum-of-bst/
#
# Description:
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
#
# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
#
# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
#
# Constraints:
# - The number of nodes in the tree is in the range [1, 2 * 10^4].
# - 1 <= Node.val <= 10^5
# - 1 <= low <= high <= 10^5
# - All Node.val are unique.

from typing import Optional
from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ✅ DFS Recursive (Depth-First Search)
def range_sum_bst_dfs_recursive(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    DFS Recursive approach to compute the sum of BST nodes within range [low, high].

    Time Complexity: O(N) in worst case, O(log N) in balanced BST.
    Space Complexity: O(H) due to recursive call stack (H is tree height).

    Parameters:
        root (TreeNode): The root node of the BST.
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: The sum of all nodes within the given range.
    """
    if not root:
        return 0

    total = 0
    if low <= root.val <= high:
        total += root.val
    
    if root.val > low:  # Left subtree may have nodes in range
        total += range_sum_bst_dfs_recursive(root.left, low, high)
    
    if root.val < high:  # Right subtree may have nodes in range
        total += range_sum_bst_dfs_recursive(root.right, low, high)
    
    return total


# ✅ DFS Iterative (Using Stack)
def range_sum_bst_dfs_iterative(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    DFS Iterative approach using a stack.

    Time Complexity: O(N) worst case.
    Space Complexity: O(H) (stack storage for tree height).

    Parameters:
        root (TreeNode): The root node of the BST.
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: The sum of all nodes within the given range.
    """
    stack = [root]
    total = 0
    
    while stack:
        node = stack.pop()
        if node:
            if low <= node.val <= high:
                total += node.val
            if node.val > low:  # Left subtree may contain valid nodes
                stack.append(node.left)
            if node.val < high:  # Right subtree may contain valid nodes
                stack.append(node.right)
    
    return total


# ✅ BFS (Breadth-First Search)
def range_sum_bst_bfs(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    BFS approach using a queue.

    Time Complexity: O(N) worst case.
    Space Complexity: O(N) (queue can store all nodes in the worst case).

    Parameters:
        root (TreeNode): The root node of the BST.
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: The sum of all nodes within the given range.
    """
    queue = deque([root])
    total = 0
    
    while queue:
        node = queue.popleft()
        if node:
            if low <= node.val <= high:
                total += node.val
            if node.val > low:  # Left subtree may contain valid nodes
                queue.append(node.left)
            if node.val < high:  # Right subtree may contain valid nodes
                queue.append(node.right)
    
    return total


# ✅ Optimized Solution (Exploiting BST properties)
def range_sum_bst_optimized(root: Optional[TreeNode], low: int, high: int) -> int:
    """
    Optimized DFS solution leveraging BST properties.

    - If root.val < low, search only in the right subtree.
    - If root.val > high, search only in the left subtree.
    - Otherwise, process the current node and search both subtrees.

    Time Complexity: O(N) worst case, O(log N) for balanced BST.
    Space Complexity: O(H) (recursive stack).

    Parameters:
        root (TreeNode): The root node of the BST.
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: The sum of all nodes within the given range.
    """
    if not root:
        return 0

    if root.val < low:
        return range_sum_bst_optimized(root.right, low, high)
    elif root.val > high:
        return range_sum_bst_optimized(root.left, low, high)
    else:
        return root.val + range_sum_bst_optimized(root.left, low, high) + range_sum_bst_optimized(root.right, low, high)


# Example test cases:
root = TreeNode(10,
                left=TreeNode(5, TreeNode(3), TreeNode(7)),
                right=TreeNode(15, None, TreeNode(18)))

print(range_sum_bst_dfs_recursive(root, 7, 15))  # Expected output: 32
print(range_sum_bst_dfs_iterative(root, 7, 15))  # Expected output: 32
print(range_sum_bst_bfs(root, 7, 15))            # Expected output: 32
print(range_sum_bst_optimized(root, 7, 15))      # Expected output: 32


# Time and Space Complexity Analysis:
#
# 1️⃣ DFS Recursive (range_sum_bst_dfs_recursive):
#   - Time Complexity: O(N) worst case, O(log N) for balanced BST.
#   - Space Complexity: O(H) due to recursion stack.
#
# 2️⃣ DFS Iterative (range_sum_bst_dfs_iterative):
#   - Time Complexity: O(N) worst case.
#   - Space Complexity: O(H) (stack storage for tree height).
#
# 3️⃣ BFS (range_sum_bst_bfs):
#   - Time Complexity: O(N) worst case.
#   - Space Complexity: O(N) (queue can store all nodes in the worst case).
#
# 4️⃣ Optimized DFS (range_sum_bst_optimized):
#   - Time Complexity: O(N) worst case, O(log N) for balanced BST.
#   - Space Complexity: O(H) (recursive stack).
