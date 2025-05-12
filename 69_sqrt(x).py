"""
🔷 LeetCode 69 – Sqrt(x)

🧠 Problem Summary:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
Do not use built-in exponent functions or operators.

✅ Constraints:
- 0 <= x <= 2^31 - 1

---

📌 Examples:

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2

---

💡 Core Idea:
Use binary search to find the integer square root.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))  # 2
    print(sol.mySqrt(8))  # 2
    print(sol.mySqrt(0))  # 0
    print(sol.mySqrt(1))  # 1

"""
⏱ Time Complexity: O(log x)
- Binary search over [1, x // 2]

💾 Space Complexity: O(1)
- Constant extra space
"""
