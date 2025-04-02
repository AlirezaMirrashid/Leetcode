"""
🔵 LeetCode 270: Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value (floating point), find the value in the BST 
that is closest to the target. You are guaranteed to have only one unique value in the BST that is 
closest to the target.

-----------------------------------
Example:
Input: root = [4,2,5,1,3], target = 3.714286

        4
       / \
      2   5
     / \
    1   3

Output: 4
Explanation: The value 4 is the closest to the target 3.714286 in the given BST.

-----------------------------------
Constraints:
    - The BST is non-empty.
    - The target is a floating point.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def closestValue(root: TreeNode, target: float) -> int:
    """
    Finds the value in the BST that is closest to the given target.

    Approach:
      - Initialize the closest value as the root's value.
      - Traverse the BST iteratively using the BST property:
            * If the current node's value is closer to target than the current closest, update the closest.
            * If target is less than the current node's value, move to the left child.
            * Otherwise, move to the right child.
      - Continue until the traversal is complete.
    
    Time Complexity: O(h), where h is the height of the BST.
    Space Complexity: O(1), since only constant extra space is used.
    
    Args:
        root (TreeNode): The root node of the BST.
        target (float): The target value to find the closest number to.
    
    Returns:
        int: The value in the BST that is closest to the target.
    """
    closest = root.val
    current = root
    while current:
        if abs(current.val - target) < abs(closest - target):
            closest = current.val
        # Traverse according to BST properties
        if target < current.val:
            current = current.left
        else:
            current = current.right
    return closest

# Sample Test Cases
if __name__ == "__main__":
    # Construct the BST:
    #         4
    #        / \
    #       2   5
    #      / \
    #     1   3
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node5 = TreeNode(5)
    root = TreeNode(4, node2, node5)
    
    target = 3.714286
    print("Example Output:", closestValue(root, target))  # Expected: 4

# ------------------------------------------------
# ✅ Time Complexity: O(h), where h is the height of the BST.
# ✅ Space Complexity: O(1), as the algorithm uses constant extra space.
