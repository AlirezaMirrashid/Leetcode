"""
🔷 LeetCode 523 - Continuous Subarray Sum (Medium)

🧠 Task:
Given an integer array `nums` and an integer `k`, return True if the array has a **good subarray**, or False otherwise.

A **good subarray**:
- Has a length of **at least two**.
- The **sum** of its elements is a **multiple of `k`**.

📘 Notes:
- A subarray is **contiguous**.
- An integer `x` is a multiple of `k` if there exists some integer `n` such that `x = n * k`.
- `0` is always a multiple of `k`.

------------------------------------------------------------
🧪 Examples:

Input: nums = [23,2,4,6,7], k = 6  
Output: True  
Explanation: Subarray [2, 4] sums to 6, which is a multiple of 6.

Input: nums = [23,2,6,4,7], k = 6  
Output: True  
Explanation: Subarray [23, 2, 6, 4, 7] sums to 42, which is 7 * 6.

Input: nums = [23,2,6,4,7], k = 13  
Output: False

------------------------------------------------------------
🔒 Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums) <= 2^31 - 1
- 1 <= k <= 2^31 - 1
"""

# ------------------------------------------------------------
# ✅ Efficient Approach: Prefix Sum + HashMap (mod trick)
# ------------------------------------------------------------

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        Keep track of the cumulative sum modulo k and use a hashmap to store the first index where each mod was seen.
        If the same mod appears again at a later index, the subarray in between is divisible by k.

        ⏱ Time: O(n)
        💾 Space: O(min(n, k))
        """
        mod_map = {0: -1}  # maps mod value to the earliest index it was seen
        cum_sum = 0

        for i, num in enumerate(nums):
            cum_sum += num
            mod = cum_sum % k

            if mod in mod_map:
                if i - mod_map[mod] >= 2:
                    return True
            else:
                mod_map[mod] = i

        return False


# ------------------------------------------------------------
# 🔍 Explanation:
# ------------------------------------------------------------
# Let sum(i, j) = prefix[j] - prefix[i - 1]
# If (prefix[j] - prefix[i - 1]) % k == 0, then prefix[j] % k == prefix[i - 1] % k
# So, we store prefix sums modulo k, and if we see a repeated mod with at least 2 elements apart, we found our subarray.

# ------------------------------------------------------------
# 🧪 Example Dry Run:
# nums = [23, 2, 4, 6, 7], k = 6
# prefix = [0, 23, 25, 29, 35, 42]
# prefix mod k = [0, 5, 1, 5, 5, 0]
# First time we see mod 5 at index 1, then again at index 3 → (3 - 1 >= 2) → subarray [2, 4] → True

# ------------------------------------------------------------
# 🧪 Test Cases:
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))     # ✅ True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))     # ✅ True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))    # ✅ False
    print(sol.checkSubarraySum([0, 0], 1))               # ✅ True (edge case: two zeros)
    print(sol.checkSubarraySum([1, 0], 2))               # ✅ False

# ------------------------------------------------------------
# ✅ Time Complexity: O(n)
# ✅ Space Complexity: O(min(n, k)) — size of the hashmap
