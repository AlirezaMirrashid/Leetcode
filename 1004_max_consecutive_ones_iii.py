"""
🔷 LeetCode 1004 - Max Consecutive Ones III

🧠 Task:
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` zeroes to `1`.

-----------------------------------
Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0's at indices 5 and 10 to get
[1,1,1,0,0,1,1,1,1,1,1]; the longest subarray of 1's is length 6.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: Flip three 0's to maximize consecutive 1's.

-----------------------------------
Constraints:
    - 1 <= nums.length <= 10^5
    - nums[i] is 0 or 1.
    - 0 <= k <= nums.length

Follow-up: Could you solve this in O(n) time?
"""
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        ✅ Optimal Sliding Window

        Maintain a window [left, right] with at most k zeros inside.
        Expand right; when zeros exceed k, move left until zeros <= k.
        Track max window length.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        max_len = 0
        zero_count = 0
        for right, val in enumerate(nums):
            if val == 0:
                zero_count += 1
            # shrink window if too many zeros
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # window [left..right] has <= k zeros
            max_len = max(max_len, right - left + 1)
        return max_len

    def longestOnesBruteForce(self, nums: List[int], k: int) -> int:
        """
        ❌ Brute Force (O(n^2))

        For each start index i, expand end j and count zeros in window;
        stop when zeros > k; track max length.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        max_len = 0
        for i in range(n):
            zero_count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zero_count += 1
                if zero_count > k:
                    break
                max_len = max(max_len, j - i + 1)
        return max_len

# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Expected: 6
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Expected: 10
    # Brute force for small cases
    print(sol.longestOnesBruteForce([1,0,1,1,0], 1))  # Expected: 4
    print(sol.longestOnesBruteForce([0,1,1,0,1], 2))  # Expected: 5
