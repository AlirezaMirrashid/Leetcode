# LeetCode 199: Binary Tree Right Side View
# Problem Link: https://leetcode.com/problems/binary-tree-right-side-view/
#
# Description:
# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
#
# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]
#
# Example 4:
# Input: root = []
# Output: []
#
# Constraints:
# - The number of nodes in the tree is in the range [0, 100].
# - -100 <= Node.val <= 100

from typing import List, Optional
from collections import deque

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView_bfs(root: Optional[TreeNode]) -> List[int]:
    """
    BFS approach to return the right side view of a binary tree.
    
    The function uses level-order traversal (BFS) and collects the last node in each level.
    
    Parameters:
        root (Optional[TreeNode]): The root of the binary tree.
        
    Returns:
        List[int]: The list of node values visible from the right side.
    """
    if not root:
        return []
    
    view = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        # Traverse nodes in the current level.
        for i in range(level_length):
            node = queue.popleft()
            # If this is the last node of the level, add it to the view.
            if i == level_length - 1:
                view.append(node.val)
            # Add left and right children to the queue.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return view


def rightSideView_dfs(root: Optional[TreeNode]) -> List[int]:
    """
    DFS approach to return the right side view of a binary tree.
    
    This function performs a depth-first search (preorder traversal) starting from the root,
    exploring the right subtree first. It records the first node encountered at each depth level,
    which corresponds to the rightmost node.
    
    Parameters:
        root (Optional[TreeNode]): The root of the binary tree.
    
    Returns:
        List[int]: The list of node values visible from the right side.
    """
    view = []
    
    def dfs(node: Optional[TreeNode], depth: int) -> None:
        if not node:
            return
        # If this is the first node we're visiting at this depth, add it to the view.
        if depth == len(view):
            view.append(node.val)
        # Traverse right subtree first, then left subtree.
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    
    dfs(root, 0)
    return view


# Example Test Cases:

if __name__ == "__main__":
    # Helper function to build a tree from list input (None represents missing nodes).
    def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = deque([root])
        index = 1
        while queue and index < len(nodes):
            node = queue.popleft()
            if index < len(nodes) and nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1
            if index < len(nodes) and nodes[index] is not None:
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1
        return root

    # Example 1:
    tree1 = build_tree([1, 2, 3, None, 5, None, 4])
    print("BFS Right Side View (Example 1):", rightSideView_bfs(tree1))  # Expected output: [1, 3, 4]
    print("DFS Right Side View (Example 1):", rightSideView_dfs(tree1))  # Expected output: [1, 3, 4]

    # Example 2:
    tree2 = build_tree([1, 2, 3, 4, None, None, None, 5])
    print("BFS Right Side View (Example 2):", rightSideView_bfs(tree2))  # Expected output: [1, 3, 4, 5]
    print("DFS Right Side View (Example 2):", rightSideView_dfs(tree2))  # Expected output: [1, 3, 4, 5]

    # Example 3:
    tree3 = build_tree([1, None, 3])
    print("BFS Right Side View (Example 3):", rightSideView_bfs(tree3))  # Expected output: [1, 3]
    print("DFS Right Side View (Example 3):", rightSideView_dfs(tree3))  # Expected output: [1, 3]

    # Example 4:
    tree4 = build_tree([])
    print("BFS Right Side View (Example 4):", rightSideView_bfs(tree4))  # Expected output: []
    print("DFS Right Side View (Example 4):", rightSideView_dfs(tree4))  # Expected output: []
    
# Time and Space Complexity Analysis:
#
# 1️⃣ BFS Approach:
#   - Time Complexity: O(N), where N is the number of nodes in the tree.
#   - Space Complexity: O(N) in the worst-case scenario (e.g., a complete tree's last level).
#
# 2️⃣ DFS Approach:
#   - Time Complexity: O(N), as we traverse each node exactly once.
#   - Space Complexity: O(H) due to the recursion stack, where H is the height of the tree.
