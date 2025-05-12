"""
🔷 LeetCode 57 – Insert Interval

🧠 Problem Summary:
Given a list of non-overlapping, sorted intervals, and a new interval,
insert the new interval and merge if necessary, returning the final list.

✅ Constraints:
- 0 <= intervals.length <= 10⁴
- 0 <= starti <= endi <= 10⁵
- intervals sorted by starti in ascending order
- newInterval is [start, end]

---

📌 Examples:

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]

---

💡 Core Idea:
- Iterate over intervals.
- Add intervals before newInterval.
- Merge overlapping intervals.
- Add intervals after newInterval.

"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))  # [[1,5],[6,9]]
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
    print(sol.insert([], [5,7]))  # [[5,7]]
    print(sol.insert([[1,5]], [2,3]))  # [[1,5]]
    print(sol.insert([[1,5]], [2,7]))  # [[1,7]]

"""
⏱ Time Complexity: O(n)
- One pass over intervals

💾 Space Complexity: O(n)
- For result list
"""
