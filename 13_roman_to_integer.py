 """
🔷 LeetCode 13 – Roman to Integer

🧠 Problem Summary:
Convert a Roman numeral string into its corresponding integer value.

📜 Roman Numerals Mapping:
Symbol | Value
-------|------
I      | 1
V      | 5
X      | 10
L      | 50
C      | 100
D      | 500
M      | 1000

🔁 Special Cases (Subtraction Rule):
- I before V or X → 4, 9
- X before L or C → 40, 90
- C before D or M → 400, 900

---

📌 Example:

Input: s = "MCMXCIV"
Output: 1994
Explanation:
M (1000) + CM (900) + XC (90) + IV (4) = 1994

---

💡 Approach:
- Traverse from left to right.
- Subtract value if current symbol is smaller than the next.
- Otherwise, add its value.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0

        for char in reversed(s):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        
        return total


# 🔸 Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))       # Output: 3
    print(sol.romanToInt("LVIII"))     # Output: 58
    print(sol.romanToInt("MCMXCIV"))   # Output: 1994

"""
⏱ Time Complexity: O(n)
    - Single pass over the string of length n

💾 Space Complexity: O(1)
    - Fixed-size dictionary and constant extra variables
"""
