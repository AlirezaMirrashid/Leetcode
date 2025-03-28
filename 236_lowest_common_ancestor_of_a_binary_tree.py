# LeetCode 236: Lowest Common Ancestor of a Binary Tree
# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Description:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself)."
#
# Example 1:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.
#
# Example 3:
# Input: root = [1, 2], p = 1, q = 2
# Output: 1
#
# Constraints:
# - The number of nodes in the tree is in the range [2, 10^5].
# - -10^9 <= Node.val <= 10^9
# - All Node.val are unique.
# - p != q
# - p and q will exist in the tree.

from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, target, path):
    """Helper function to find the path from root to the target node."""
    if not root:
        return False
    path.append(root)

    if root == target:
        return True

    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True

    path.pop()  # Backtrack if target is not found in this path
    return False


def lowest_common_ancestor_bt_brute_force(root, p, q):
    """
    Brute force approach to find the lowest common ancestor (LCA) of two nodes in a binary tree.

    Steps:
    - Find the path from the root to node p.
    - Find the path from the root to node q.
    - Compare paths to find the last common node before they diverge.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    path_p, path_q = [], []

    if not find_path(root, p, path_p) or not find_path(root, q, path_q):
        return None  # One of the nodes is not present in the tree

    # Compare paths to find the last common node
    lca = None
    for a, b in zip(path_p, path_q):
        if a == b:
            lca = a
        else:
            break

    return lca


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a binary tree.

    The function uses recursion to traverse the tree. If the current root is either of the given nodes,
    it returns the root. Otherwise, it recursively searches in both left and right subtrees.

    If both left and right recursive calls return non-null values, the current root is the LCA.
    If only one side returns a node, that means both nodes are found within the same subtree,
    so it returns the non-null result.

    Parameters:
        root (Optional[TreeNode]): The root of the binary tree.
        p (TreeNode): The first node.
        q (TreeNode): The second node.

    Returns:
        Optional[TreeNode]: The lowest common ancestor of nodes p and q.

    Time Complexity:
        - O(N), where N is the number of nodes in the tree.
        - In the worst case, we visit all nodes to find p and q.

    Space Complexity:
        - O(H), where H is the height of the tree (O(log N) for balanced trees, O(N) for skewed trees).
        - This accounts for the recursive stack depth.

    Examples:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(1)
        >>> root.left.left = TreeNode(6)
        >>> root.left.right = TreeNode(2)
        >>> root.right.left = TreeNode(0)
        >>> root.right.right = TreeNode(8)
        >>> p = root.left  # Node with value 5
        >>> q = root.right  # Node with value 1
        >>> lowest_common_ancestor(root, p, q).val
        3
    """
    if not root:
        return None
    if root == p or root == q:
        return root

    left_subtree = lowest_common_ancestor(root.left, p, q)
    right_subtree = lowest_common_ancestor(root.right, p, q)

    if left_subtree and right_subtree:
        return root  # If p and q are found in different subtrees, root is the LCA.

    return left_subtree or right_subtree  # Return the non-null node if both nodes are in one subtree.


# Example test cases:
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with value 5
    q = root.right  # Node with value 1
    print(lowest_common_ancestor(root, p, q).val)  # Expected output: 3

    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4
    print(lowest_common_ancestor(root, p, q).val)  # Expected output: 5

    p = root  # Node with value 3
    q = root.right.right  # Node with value 8
    print(lowest_common_ancestor(root, p, q).val)  # Expected output: 3
