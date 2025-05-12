"""
🔷 LeetCode 2 - Add Two Numbers

🧠 Problem Summary:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

✳️ Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- The numbers do not contain leading zeroes except for the number 0 itself.

📌 Examples:

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # current digit from l1
            val2 = l2.val if l2 else 0  # current digit from l2

            total = val1 + val2 + carry
            carry = total // 10  # update carry
            current.next = ListNode(total % 10)  # create new node with current digit
            current = current.next

            # Move to next digits
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# 🔸 Helper functions for testing
def list_to_linkedlist(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# 🔸 Example usage
if __name__ == "__main__":
    sol = Solution()
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print(linkedlist_to_list(result))  # ➞ [7, 0, 8]
"""

🧠 Time and Space Complexity:

⏱ Time Complexity: O(max(m, n))
- We traverse both linked lists once, where m and n are the lengths of the input lists.

💾 Space Complexity: O(max(m, n))
- We create a new linked list whose length is at most max(m, n) + 1 due to carry.
"""

