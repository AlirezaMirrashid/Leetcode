"""
🔷 LeetCode 23 – Merge k Sorted Lists
📘 Problem Statement:
You are given an array of k linked-lists, each linked list is sorted in ascending order.
Merge all the linked lists into one sorted linked list and return the merged list.

✏️ Input:
lists[i] is a sorted linked list.

0 <= k <= 10⁴

0 <= lists[i].length <= 500

-10⁴ <= lists[i][j] <= 10⁴

The total number of nodes across all lists does not exceed 10⁴.

✅ Output:
Return one sorted linked list containing all elements from the input lists.

🧠 Example:
Input:  lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation:
  Merge lists:
    1→4→5
    1→3→4
    2→6
  Result:
    1→1→2→3→4→4→5→6
"""

from typing import List, Optional

# 🔹 Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        ✅ Merge two sorted linked lists into one sorted list.
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach remaining part (only one will be non-null)
        tail.next = l1 or l2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        ✅ Merge k sorted linked lists using pairwise merge (divide & conquer).
        """
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged  # Reduce problem size by half each round

        return lists[0]


"""
 Time Complexity:
Each merge: O(n), where n is total nodes being merged.

Log k rounds of merging → Total time = O(N log k).

💾 Space Complexity:
O(1) extra (no heap, no recursion).

O(N) for final output.
"""
