"""
🔷 LeetCode 636 - Exclusive Time of Functions

📘 Description:
You are given a list of logs from a single-threaded CPU executing a program with n functions (IDs 0 to n-1).
Each log is in the format: "{function_id}:{start|end}:{timestamp}"

A function's exclusive time is the sum of time units it spends executing on the CPU, excluding the time spent
by other functions that it called.

Return a list where the i-th element is the exclusive time for the function with ID i.

---

🧪 Examples:

Example 1:
Input: 
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: 
    [3, 4]
Explanation:
    Function 0 starts at 0, pauses at 2
    Function 1 runs from 2 to 5 (4 units), ends at 5
    Function 0 resumes at 6, ends at 6 → total: (2-0) + (6-6+1) = 3
    Function 1: 5 - 2 + 1 = 4

Example 2:
Input:
    n = 1
    logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output:
    [8]

---

💡 Constraints:
- 1 <= n <= 100
- 1 <= logs.length <= 500
- 0 <= function_id < n
- 0 <= timestamp <= 1e9
- Logs are properly nested with no overlaps.
"""

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        ✅ Stack-based solution to track nested calls and timestamps.

        At every log:
            - If "start": pause the previous function (if any) and push the new one.
            - If "end": compute time for top function and pop it.

        Time is tracked using `prev_time` to accumulate durations.
        """
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid_str, typ, time_str = log.split(":")
            fid, timestamp = int(fid_str), int(time_str)

            if typ == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fid)
                prev_time = timestamp
            else:  # "end"
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res


# 🔸 Sample test cases
if __name__ == "__main__":
    sol = Solution()

    logs1 = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    print(sol.exclusiveTime(2, logs1))  # ➞ [3, 4]

    logs2 = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
    print(sol.exclusiveTime(1, logs2))  # ➞ [8]

    logs3 = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    print(sol.exclusiveTime(2, logs3))  # ➞ [7, 1]


"""
--------------------------------------------------------
⏱ Time Complexity: O(L), where L is the number of log entries.
    - Each log is parsed and processed once.

💾 Space Complexity: O(n + L)
    - O(n) for result list.
    - O(L) in worst-case for the stack (nested calls).
"""

