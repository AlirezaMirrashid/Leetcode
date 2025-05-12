"""
🔷 LeetCode 173 – Binary Search Tree Iterator

🧠 Problem Summary:
Design an iterator over a BST that returns the next smallest number in in-order traversal.

✅ Requirements:
- `next()` should return the next smallest element.
- `hasNext()` should return whether there's a next element.
- Must support average O(1) time per operation and O(h) space, where h is tree height.

---

📌 Example:
Input:
BST =        7
           /   \
         3     15
              /  \
             9    20

Traversal order: [3, 7, 9, 15, 20]
Operations:
BSTIterator bSTIterator = new BSTIterator(root);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
...

---

💡 Core Idea:
- Use a stack to simulate in-order traversal.
- Push all leftmost nodes to the stack at initialization and when moving right.
- This ensures O(h) space and average O(1) time per operation.

"""

# 🔹 Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node: TreeNode):
        # Go as left as possible
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Top of the stack is the next smallest element
        node = self.stack.pop()
        val = node.val
        # If there's a right subtree, process its leftmost nodes
        if node.right:
            self._leftmost_inorder(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# -------------------------
# 🔸 Example test run (manual tree construction)
if __name__ == "__main__":
    # Construct the tree: [7, 3, 15, null, null, 9, 20]
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15, TreeNode(9), TreeNode(20))

    bst_iter = BSTIterator(root)
    print(bst_iter.next())    # 3
    print(bst_iter.next())    # 7
    print(bst_iter.hasNext()) # True
    print(bst_iter.next())    # 9
    print(bst_iter.hasNext()) # True
    print(bst_iter.next())    # 15
    print(bst_iter.hasNext()) # True
    print(bst_iter.next())    # 20
    print(bst_iter.hasNext()) # False

"""
⏱ Time Complexity:
- next(): Amortized O(1) over all n calls
- hasNext(): O(1)

💾 Space Complexity: O(h), where h is the height of the BST (due to the stack)
"""
