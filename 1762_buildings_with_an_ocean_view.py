"""
🔷 LeetCode 1762 - Buildings With an Ocean View

A building has an ocean view if all buildings to its right are shorter.

🧠 Task:
Return a list of indices of such buildings, in increasing order.
"""

from typing import List
from collections import deque

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        ✅ Right-to-left traversal, keep track of the max height seen so far.
        Append qualifying buildings to a result list and reverse at the end.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(n) (result list stores indices)
        """
        n = len(heights)
        result = []
        max_height = float('-inf')

        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        return result[::-1]

    def findBuildingsDeque(self, heights: List[int]) -> List[int]:
        """
        ✅ Deque-based version: appendleft for natural increasing order without reversing.
        Uses a deque to efficiently insert at the beginning.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(n)
        """
        dq = deque()
        max_height = float('-inf')

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                dq.appendleft(i)
                max_height = heights[i]

        return list(dq)


# 🔸 Sample test runs
if __name__ == "__main__":
    sol = Solution()
    heights_list = [
        [4, 2, 3, 1],
        [4, 3, 2, 1],
        [1, 3, 2, 4],
        [2, 2, 2, 2]
    ]

    for heights in heights_list:
        print("Input:", heights)
        print("Result (List):", sol.findBuildings(heights))
        print("Result (Deque):", sol.findBuildingsDeque(heights))
        print("------------")
