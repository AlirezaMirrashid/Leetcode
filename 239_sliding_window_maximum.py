"""
🔷 LeetCode 239: Sliding Window Maximum

🧠 Task:
Given an array of integers `nums` and a sliding window size `k`, return an array of the maximum 
value in each window as it moves from left to right by one position.

-----------------------------------
Example 1:
Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
 Window positions and their maxima:
  [1  3  -1] -3  5  3  6  7  → 3
   1 [3  -1  -3] 5  3  6  7  → 3
   1  3 [-1  -3   5] 3  6  7  → 5
   1  3  -1 [-3   5   3] 6  7  → 5
   1  3  -1  -3 [5   3   6] 7  → 6
   1  3  -1  -3  5 [3   6   7] → 7

Example 2:
Input:  nums = [1], k = 1
Output: [1]

-----------------------------------
Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length
"""

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        ✅ Optimal Approach: Monotonic Queue (Deque)

        Maintain a deque of indices whose corresponding values are in decreasing order.
        - The front of the deque is always the index of the current window’s maximum.
        - For each new index i:
          1. Remove indices from the back while nums[i] >= nums[back].
          2. Append i to the back.
          3. Remove the front if it’s outside the window (i - k).
          4. Once i >= k-1, record nums[deque[0]] as the window max.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(k)
        """
        if not nums or k == 0:
            return []

        dq = deque()  # will store indices
        result = []

        for i, num in enumerate(nums):
            # 1) Pop smaller values from back
            while dq and nums[dq[-1]] < num:
                dq.pop()

            # 2) Append current index
            dq.append(i)

            # 3) Remove front if out of window
            if dq[0] == i - k:
                dq.popleft()

            # 4) Record result once first window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

    def maxSlidingWindowBruteForce(self, nums: List[int], k: int) -> List[int]:
        """
        ❌ Brute Force Approach

        For each window start i from 0 to len(nums)-k:
          - Compute max(nums[i:i+k]) directly.

        ⏱ Time Complexity: O(n * k)
        💾 Space Complexity: O(n - k + 1) for the output list
        """
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i+k]) for i in range(n - k + 1)]


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()

    nums1, k1 = [1,3,-1,-3,5,3,6,7], 3
    print("Optimal:", sol.maxSlidingWindow(nums1, k1))          # Expected: [3,3,5,5,6,7]
    print("Brute Force:", sol.maxSlidingWindowBruteForce(nums1, k1))

    nums2, k2 = [1], 1
    print("Optimal:", sol.maxSlidingWindow(nums2, k2))          # Expected: [1]
    print("Brute Force:", sol.maxSlidingWindowBruteForce(nums2, k2))

# ------------------------------------------------
# ✅ Monotonic Queue Approach:
#     Time Complexity: O(n)
#     Space Complexity: O(k)
#
# ❌ Brute Force Approach:
#     Time Complexity: O(n·k)
#     Space Complexity: O(n - k + 1)
