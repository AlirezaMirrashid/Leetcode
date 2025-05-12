"""
🔷 LeetCode 43 – Multiply Strings

🧠 Problem Summary:
Given two non-negative integers `num1` and `num2` represented as strings,
return the product of `num1` and `num2`, also represented as a string.

✅ Constraints:
- Must not use BigInteger or convert strings directly to integers.
- num1, num2 consist of digits only.
- 1 <= num1.length, num2.length <= 200

---

📌 Example:

Input: num1 = "123", num2 = "456"
Output: "56088"
Because: 123 * 456 = 56088

---

💡 Core Idea:
Use the classical digit-by-digit multiplication method (like manual multiplication).

👉 For each digit in num1 and num2:
    - Multiply digits and store the result at the correct position in an array.
    - Handle carry for values > 9.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Reverse loop to multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1

                # Add current multiplication to previous result at p2
                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        # Convert to string, skip leading zeros
        result_str = ''.join(map(str, result)).lstrip("0")
        return result_str or "0"


# -------------------------
# 🔸 Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("123", "456"))  # "56088"
    print(sol.multiply("2", "3"))      # "6"
    print(sol.multiply("0", "99999"))  # "0"

"""
⏱ Time Complexity: O(m * n)
    - m = len(num1), n = len(num2)
    - We multiply every digit of num1 with every digit of num2

💾 Space Complexity: O(m + n)
    - For result array to store intermediate results
"""
