"""
🔷 LeetCode 238 - Product of Array Except Self

🧠 Problem Summary:
Given an integer array `nums`, return an array `answer` such that `answer[i]` 
is equal to the product of all the elements of `nums` except `nums[i]`.

🚫 Constraints:
- Do NOT use division.
- Must run in O(n) time.
- Follow-up: Can you solve it with O(1) extra space? (output array not counted)

📘 Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

📘 Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

✅ Strategy:
1. Build a `prefix` product array (left to right).
2. Build a `suffix` product while updating the result array in reverse (right to left).
3. Do it in-place using the result array to hold the left product first, and merge with right pass.
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: Prefix product (left to right)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix product (right to left)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# 🔸 Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))        # ➞ [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))   # ➞ [0, 0, 9, 0, 0]

"""
🧠 Time and Space Complexity:

⏱ Time Complexity: O(n)
- One pass for prefix and one for suffix = 2 * O(n)

💾 Space Complexity:
- O(1) extra space (excluding result array)
- We're reusing the result array for both prefix and final product
"""

