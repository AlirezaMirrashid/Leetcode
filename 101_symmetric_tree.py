"""
🔷 LeetCode 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: True
    Explanation: The tree is symmetric.

Example 2:
    Input: root = [1,2,2,None,3,None,3]
    Output: False
    Explanation: The tree is not symmetric.

Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric_recursive(root: Optional[TreeNode]) -> bool:
    """
    Recursive approach: compare left subtree and right subtree for mirror equality.
    
    Time Complexity: O(n), we visit each node once.
    Space Complexity: O(n) worst-case recursion stack (skewed tree).
    """
    def is_mirror(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2:
            return True
        if not n1 or not n2 or n1.val != n2.val:
            return False
        # Compare outside pair and inside pair
        return is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

    return is_mirror(root.left, root.right) if root else True

def isSymmetric_iterative(root: Optional[TreeNode]) -> bool:
    """
    Iterative approach using a queue (BFS-like): push pairs of nodes to compare.
    
    Time Complexity: O(n), we process each node once.
    Space Complexity: O(n) for the queue in the worst case.
    """
    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        n1, n2 = queue.popleft()
        if not n1 and not n2:
            continue
        if not n1 or not n2 or n1.val != n2.val:
            return False
        # enqueue children in mirror order
        queue.append((n1.left, n2.right))
        queue.append((n1.right, n2.left))
    return True

# ---------- Helper to build tree from list input for testing ----------
def build_tree(vals):
    """
    Build a binary tree from level-order list `vals` where None indicates missing node.
    Returns the root TreeNode.
    """
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if node:
            left_val = vals[i] if i < len(vals) else None
            right_val = vals[i+1] if i+1 < len(vals) else None
            node.left = TreeNode(left_val) if left_val is not None else None
            node.right = TreeNode(right_val) if right_val is not None else None
            queue.append(node.left)
            queue.append(node.right)
            i += 2
    return root

# ------------- Sample tests -------------
if __name__ == "__main__":
    tests = [
        ([1,2,2,3,4,4,3], True),
        ([1,2,2,None,3,None,3], False),
        ([1,2,2,2,None,2], False),
        ([1], True),
        ([], True),
    ]
    for vals, expected in tests:
        root = build_tree(vals)
        out_rec = isSymmetric_recursive(root)
        out_it  = isSymmetric_iterative(root)
        print(f"Tree {vals!r:20} → recursive: {out_rec}, iterative: {out_it}, expected: {expected}")

"""
✅ Complexity:
- Recursive:
    Time:  O(n)
    Space: O(n) (recursion stack)
- Iterative:
    Time:  O(n)
    Space: O(n) (queue)
"""
