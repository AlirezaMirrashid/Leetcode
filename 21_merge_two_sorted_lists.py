"""
🔷 LeetCode 21 – Merge Two Sorted Lists

🧠 Problem Summary:
Given the heads of two sorted linked lists, merge them into one sorted list by splicing their nodes together.

✅ Constraints:
- Number of nodes: 0–50
- Node values: -100 to 100
- Both lists sorted in non-decreasing order

---

📌 Example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

---

💡 Solution 1 (Iterative):
- Use a dummy node
- Compare nodes and attach the smaller one

💡 Solution 2 (Recursive):
- Base case: if one list is empty, return the other
- Recur on smaller head
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoListsIterative(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

    def mergeTwoListsRecursive(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2


# -------------------------
# 🔸 Example helper to build and print lists
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == "__main__":
    sol = Solution()
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    merged = sol.mergeTwoListsIterative(l1, l2)
    print_list(merged)  # [1,1,2,3,4,4]

    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    merged = sol.mergeTwoListsRecursive(l1, l2)
    print_list(merged)  # [1,1,2,3,4,4]

"""
⏱ Time Complexity:
- Both solutions: O(n + m), where n and m are the lengths of list1 and list2

💾 Space Complexity:
- Iterative: O(1) (in-place except dummy pointer)
- Recursive: O(n + m) call stack
"""
