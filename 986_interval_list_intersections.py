"""
🔵 LeetCode 986 - Interval List Intersections

You are given two lists of closed intervals:
- firstList[i] = [start_i, end_i]
- secondList[j] = [start_j, end_j]

Each list is pairwise disjoint and sorted. Return their intersections.

---

Example 1:
Input: 
firstList = [[0,2],[5,10],[13,23],[24,25]], 
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

---

Constraints:
- 0 <= firstList.length, secondList.length <= 1000
- firstList and secondList are sorted and non-overlapping
- 0 <= starti < endi <= 10⁹
- endi < start(i+1)

"""

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        ✅ Two-pointer solution.
        Traverse both lists simultaneously and find overlapping intervals.

        ⏱ Time Complexity: O(n + m), where n and m are lengths of firstList and secondList.
        💾 Space Complexity: O(1) (ignoring output list)
        """
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            # Check if intervals overlap
            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                result.append([start, end])

            # Move the pointer with smaller end
            if a_end < b_end:
                i += 1
            else:
                j += 1

        return result


# 🔹 Sample Test
if __name__ == "__main__":
    sol = Solution()
    first = [[0,2],[5,10],[13,23],[24,25]]
    second = [[1,5],[8,12],[15,24],[25,26]]
    print(sol.intervalIntersection(first, second))
    # ➞ [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


