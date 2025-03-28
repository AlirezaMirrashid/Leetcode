# LeetCode 314: Binary Tree Vertical Order Traversal
# Problem Link: https://leetcode.com/problems/binary-tree-vertical-order-traversal/

"""
Description:
Given the root of a binary tree, return the vertical order traversal of its nodes' values.
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[9], [3, 15], [20], [7]]

Example 2:
Input: root = [3, 9, 8, 4, 0, 1, 7]
Output: [[4], [9], [3, 0, 1], [8], [7]]

Example 3:
Input: root = [1, 2, 3, 4, 10, 9, 11, null, 5, null, null, null, null, null, null, null, 6]
Output: [[4], [2, 5], [1, 10, 9, 6], [3], [11]]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Solution 1: DFS (Depth First Search)
In this approach, we traverse the binary tree using DFS. During the traversal, we record each node's value, depth, and horizontal offset (column number).
Then, we sort the nodes by their column number (from left to right) and their depth (from top to bottom).
After sorting, we group the nodes by their column numbers to get the final vertical order.

Time complexity: O(n log n) - Sorting the nodes based on column offset and depth takes O(n log n) time, where n is the number of nodes.
Space complexity: O(n) - We use a defaultdict to store nodes grouped by their column offset, which can hold up to n nodes.

"""

from collections import defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, depth, offset):
            if root is None:
                return
            # Add the current node's value along with its depth to the corresponding column (offset)
            column_dict[offset].append((depth, root.val))
            # Traverse the left child with offset - 1 (go left decreases column)
            dfs(root.left, depth + 1, offset - 1)
            # Traverse the right child with offset + 1 (go right increases column)
            dfs(root.right, depth + 1, offset + 1)

        column_dict = defaultdict(list)  # To store nodes grouped by their column number
        dfs(root, 0, 0)  # Start DFS with root at depth 0 and column offset 0

        result = []
        # Sort the columns by their offset (column number)
        for _, values in sorted(column_dict.items()):
            # Sort the nodes within the same column by depth
            values.sort(key=lambda x: x[0])
            result.append([val for _, val in values])  # Extract node values in sorted order
        return result


"""
Solution 2: BFS (Breadth First Search)
In this approach, we use BFS to traverse the tree level by level, ensuring that we visit nodes from top to bottom. During BFS, we record the column offset of each node.
We then group nodes by their column offsets and return the vertical order.

Time complexity: O(n) - BFS visits each node once, and sorting the columns takes O(n log n).
Space complexity: O(n) - We use a queue and a defaultdict to store nodes, so the space complexity is linear.

"""

from collections import deque, defaultdict
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root, 0)])  # Queue for BFS: stores nodes and their column offsets
        column_dict = defaultdict(list)  # Dictionary to store nodes grouped by their column offset
        min_offset, max_offset = 0, 0  # To track the range of column offsets

        # Perform BFS
        while queue:
            for _ in range(len(queue)):
                node, offset = queue.popleft()
                column_dict[offset].append(node.val)
                min_offset = min(min_offset, offset)  # Update the min column offset
                max_offset = max(max_offset, offset)  # Update the max column offset

                if node.left:
                    queue.append((node.left, offset - 1))  # Add left child with offset - 1
                if node.right:
                    queue.append((node.right, offset + 1))  # Add right child with offset + 1

        # # Return nodes sorted by their column offsets
        # return [column_dict[key] for key in sorted(column_dict.keys())]
        # Return nodes grouped by column, iterating directly from min to max column offsets
        return [column_dict[i] for i in range(min_offset, max_offset + 1)]

"""
Time and Space Complexity Analysis:
Time Complexity:
- **O(n log n)** for DFS (Solution 1), due to sorting the nodes by their depth and column offset.
- # **O(n)** for BFS (Solution 2), since each node is visited once and we only sort the keys of the dictionary at the end. 
- **O(n)** for BFS (Solution 2), since each node is processed once, and we avoid sorting by directly iterating through the column offsets in the range between `min_offset` and `max_offset`. This makes the BFS approach more efficient (number of keys could be as large as n and we should avoid sorting).

Space Complexity:
- **O(n)** for both approaches, because we store up to n nodes in the `column_dict` (and BFS also uses a queue of up to n nodes at once).
"""
