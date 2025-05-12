"""
🔷 LeetCode 206 – Reverse Linked List

🧠 Problem Summary:
Given the head of a singly linked list, reverse the list and return the new head.

✅ Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000

---

📌 Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

📌 Example 2:
Input: head = [1,2]
Output: [2,1]

📌 Example 3:
Input: head = []
Output: []

---

💡 Core Idea:
Reverse the linked list by:
1. Iteratively updating the next pointers.
2. Recursively flipping each pair of connections until the end.
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        # Helper to print a list from current node to end
        vals = []
        current = self
        while current:
            vals.append(current.val)
            current = current.next
        return str(vals)

class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ✅ Iterative solution to reverse a linked list.
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # store next node
            curr.next = prev       # reverse pointer
            prev = curr            # move prev forward
            curr = next_node       # move curr forward
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        ✅ Recursive solution to reverse a linked list.
        """
        if not head or not head.next:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


# 🔸 Helper to build list from Python list
def build_linked_list(values):
    if not values: return None
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# 🔸 Test Cases
if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([1, 2, 3, 4, 5])
    print("Iterative:", sol.reverseList_iterative(head1))  # [5, 4, 3, 2, 1]

    head2 = build_linked_list([1, 2])
    print("Recursive:", sol.reverseList_recursive(head2))  # [2, 1]

    head3 = build_linked_list([])
    print("Empty list:", sol.reverseList_iterative(head3))  # []

"""
⏱ Time Complexity: O(n) – Each node is visited once.
💾 Space Complexity:
- Iterative: O(1)
- Recursive: O(n) for recursion stack
"""
