# LeetCode 235: Lowest Common Ancestor of a Binary Search Tree
# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Description:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a descendant of itself)."
#
# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
#
# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
# Constraints:
# - The number of nodes in the tree is in the range [2, 10^5].
# - -10^9 <= Node.val <= 10^9
# - All Node.val are unique.
# - p != q
# - p and q will exist in the BST.

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
def lowest_common_ancestor_bst_brute_force(root, p, q):
    """
    Brute force approach to find the lowest common ancestor (LCA) of two nodes in a binary search tree.

    - Uses the general LCA approach for a binary tree.
    - Finds paths to p and q, then compares them.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    return lowest_common_ancestor_bt_brute_force(root, p, q)


def lowest_common_ancestor_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).

    Since it is a BST, we can use its properties:
    - If both p and q are smaller than root, LCA must be in the left subtree.
    - If both p and q are greater than root, LCA must be in the right subtree.
    - Otherwise, the root is the LCA because p and q are in different subtrees.

    Parameters:
        root (Optional[TreeNode]): The root of the BST.
        p (TreeNode): The first node.
        q (TreeNode): The second node.

    Returns:
        Optional[TreeNode]: The lowest common ancestor of nodes p and q.

    Time Complexity:
        - O(H), where H is the height of the BST.
        - O(log N) for balanced BSTs, O(N) in the worst case for a skewed BST.

    Space Complexity:
        - O(1) for the iterative approach since we use constant extra space.
        - O(H) for the recursive approach due to the call stack.

    Examples:
        >>> root = TreeNode(6)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(8)
        >>> root.left.left = TreeNode(0)
        >>> root.left.right = TreeNode(4)
        >>> root.right.left = TreeNode(7)
        >>> root.right.right = TreeNode(9)
        >>> root.left.right.left = TreeNode(3)
        >>> root.left.right.right = TreeNode(5)
        >>> p = root.left  # Node with value 2
        >>> q = root.right  # Node with value 8
        >>> lowest_common_ancestor_bst(root, p, q).val
        6
    """
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left  # Both nodes are in the left subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right  # Both nodes are in the right subtree
        else:
            return root  # Split point found, root is the LCA

    return None  # This line is just for safety; it should never be reached if p and q exist in the BST.


# Example test cases:
if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    print(lowest_common_ancestor_bst(root, p, q).val)  # Expected output: 6

    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    print(lowest_common_ancestor_bst(root, p, q).val)  # Expected output: 2

    p = root  # Node with value 6
    q = root.right.right  # Node with value 9
    print(lowest_common_ancestor_bst(root, p, q).val)  # Expected output: 6
