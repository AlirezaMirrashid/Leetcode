"""
🔁 LeetCode 708 - Insert into a Cyclic Sorted List

Given a node from a cyclic, sorted, singly linked list, insert a new node such that the list remains cyclic and sorted.

The list is not necessarily starting from the smallest element, so insertion logic must account for the list's circular nature.

----------------------
🔹 Example:

Given list (cyclic): 3 → 4 → 1 → (back to 3)
Insert: 2

Result (cyclic): 3 → 4 → 1 → 2 → (back to 3)
----------------------

Constraints:
- The list is cyclic and sorted in ascending order.
- Given node may point to any node in the list.
- The new value can be inserted at multiple valid positions.
- If the list is empty, return a new node pointing to itself.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new_node = Node(insertVal)

        # Case 1: Empty list → new node points to itself
        if not head:
            new_node.next = new_node
            return new_node

        curr = head

        while True:
            # Normal case: insertVal fits between curr and curr.next
            if curr.val <= insertVal <= curr.next.val:
                break

            # Turning point: max → min (e.g., 4 → 1), insert if out of bounds
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break

            curr = curr.next

            # If we've looped back to start, insert anywhere
            if curr == head:
                break

        # Insert the new node between curr and curr.next
        new_node.next = curr.next
        curr.next = new_node
        return head



# ✅ Time & Space:
# Time Complexity: O(n) in worst case (one full loop).

# Space Complexity: O(1)
