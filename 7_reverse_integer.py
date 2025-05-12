"""
🔷 LeetCode 7 - Reverse Integer

🧠 Problem Summary:
Given a signed 32-bit integer x, return x with its digits reversed. 
If the reversed integer overflows (outside the signed 32-bit integer range [-2^31, 2^31 - 1]), return 0.

⚠️ Constraint:
- You must not use 64-bit integers.

📌 Examples:

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

💡 Intuition:
- Pop digits from the original number and push them into a result number.
- Check overflow before pushing new digits.
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check if res * 10 + digit will overflow
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res


# 🔸 Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))     # ➞ 321
    print(sol.reverse(-123))    # ➞ -321
    print(sol.reverse(120))     # ➞ 21
    print(sol.reverse(0))       # ➞ 0
    print(sol.reverse(1534236469))  # ➞ 0 (overflow case)

"""
🧠 Time and Space Complexity:

⏱ Time Complexity: O(log₁₀x)
- Each digit is processed once (divide by 10 per step).

💾 Space Complexity: O(1)
- Constant space used for variables.
"""

