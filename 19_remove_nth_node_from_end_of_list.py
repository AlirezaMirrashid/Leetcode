"""
🔷 LeetCode 19 - Remove Nth Node From End of List

🧠 Task:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

You must do this in one pass.

-----------------------------------
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: The 2nd node from the end (node with value 4) is removed.

Example 2:
Input: head = [1], n = 1
Output: []
Explanation: Removing the only node leaves an empty list.

Example 3:
Input: head = [1,2], n = 1
Output: [1]
Explanation: The last node (node with value 2) is removed.

-----------------------------------
Constraints:
    - 1 <= sz <= 30, where sz is the number of nodes in the list.
    - 0 <= Node.val <= 100
    - 1 <= n <= sz

Follow up:
    Could you do this in one pass?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        ✅ One-Pass Two-Pointer Approach
        
        Approach:
          - Initialize two pointers, fast and slow, both starting at a dummy node (with next = head).
          - Move the fast pointer n+1 steps ahead.
          - Then, move both fast and slow pointers together until fast reaches the end.
          - The slow pointer will then point to the node before the target node.
          - Remove the target node by adjusting pointers.
        
        ⏱ Time Complexity: O(sz), where sz is the number of nodes in the list.
        💾 Space Complexity: O(1)
        
        Args:
            head (ListNode): The head of the linked list.
            n (int): The nth node from the end to remove.
        
        Returns:
            ListNode: The head of the modified linked list.
        """
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow now points to the node before the target; remove it
        slow.next = slow.next.next

        return dummy.next

    def removeNthFromEndBrute(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        ❌ Two-Pass Brute Force Approach
        
        Approach:
          - First pass: Compute the length of the linked list.
          - Second pass: Traverse to the (length - n)th node and remove its next node.
        
        ⏱ Time Complexity: O(sz)
        💾 Space Complexity: O(1)
        
        Args:
            head (ListNode): The head of the linked list.
            n (int): The nth node from the end to remove.
        
        Returns:
            ListNode: The head of the modified linked list.
        """
        dummy = ListNode(0, head)
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        current = dummy
        # Traverse to the node before the target
        for _ in range(length - n):
            current = current.next

        # Remove the target node
        current.next = current.next.next

        return dummy.next

# 🔸 Helper Function to Convert List to Linked List for Testing
def list_to_linkedlist(lst: list) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 🔸 Helper Function to Convert Linked List to List for Verification
def linkedlist_to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()

    # Example 1:
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    new_head1 = sol.removeNthFromEnd(head1, 2)
    print("Example 1 Output:", linkedlist_to_list(new_head1))  # Expected: [1,2,3,5]

    # Example 2:
    head2 = list_to_linkedlist([1])
    new_head2 = sol.removeNthFromEnd(head2, 1)
    print("Example 2 Output:", linkedlist_to_list(new_head2))  # Expected: []

    # Example 3:
    head3 = list_to_linkedlist([1, 2])
    new_head3 = sol.removeNthFromEnd(head3, 1)
    print("Example 3 Output:", linkedlist_to_list(new_head3))  # Expected: [1]

# ------------------------------------------------
# ✅ Time Complexity: O(sz), where sz is the number of nodes in the list.
# ✅ Space Complexity: O(1)
