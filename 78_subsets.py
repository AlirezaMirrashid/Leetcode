"""
🔷 LeetCode 78 – Subsets

🧠 Problem Summary:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. You may return the subsets in any order.

✅ Constraints:
- 1 <= nums.length <= 10  
- -10 <= nums[i] <= 10  
- All the numbers of nums are unique.

---

📌 Examples:

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Example 2:
Input: nums = [0]
Output: [[],[0]]


---

💡 Approaches:

1. **DFS Backtracking**  
   Recursively decide for each element whether to include it in the current subset.

2. **Iterative (Cascading) / BFS-style**  
   Start with `[[]]`. For each number, take all existing subsets and append the number to them.

3. **Bitmask Enumeration**  
   There are 2^n subsets. For mask from 0 to 2^n−1, interpret bits as inclusion/exclusion.

"""

from collections import deque
from typing import List

class Solution:
    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        """DFS backtracking solution."""
        res = []
        path = []
        n = len(nums)

        def dfs(idx: int):
            # At each call, path is a valid subset
            res.append(path.copy())
            # Try including each remaining element
            for i in range(idx, n):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res

    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        """Iterative cascading solution."""
        res = [[]]
        for num in nums:
            # For each existing subset, create a new one that includes num
            res += [curr + [num] for curr in res]
        return res

    def subsets_bitmask(self, nums: List[int]) -> List[List[int]]:
        """Bitmask enumeration solution."""
        n = len(nums)
        res = []
        for mask in range(1 << n):  # 0 to 2^n - 1
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            res.append(subset)
        return res


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
        ([0], [[],[0]]),
    ]
    for nums, _ in tests:
        print("DFS      ", sol.subsets_dfs(nums))
        print("Iterative", sol.subsets_iterative(nums))
        print("Bitmask  ", sol.subsets_bitmask(nums))
        print("----")

"""
⏱ Time Complexity:
- DFS Backtracking: O(n · 2ⁿ)
    - We generate 2ⁿ subsets, and copying each path costs O(n) in the worst case.
- Iterative Cascading: O(n · 2ⁿ)
    - For each of n numbers, we double the list of subsets (cost proportional to current size).
- Bitmask Enumeration: O(n · 2ⁿ)
    - We iterate over 2ⁿ masks, and for each mask we check n bits.

💾 Space Complexity:
- O(n · 2ⁿ) to store all subsets in the output.
- Additional auxiliary space:
  - DFS recursion uses O(n) call stack.
  - Iterative uses O(1) extra besides output.
  - Bitmask uses O(1) extra besides output.
"""


