"""
🔷 LeetCode 38 – Count and Say

🧠 Problem Summary:
The count-and-say sequence is a series of digit strings defined recursively:
- countAndSay(1) = "1"
- countAndSay(n) is the run-length encoding (RLE) of countAndSay(n - 1)

Run-Length Encoding (RLE):
It compresses strings by replacing runs of identical characters with "count + character".
Example: "3322251" → "23321511"

✅ Constraints:
- 1 <= n <= 30

---

📌 Example:

Input: n = 4  
Output: "1211"  
Explanation:
- countAndSay(1) = "1"
- countAndSay(2) = "11" (one 1)
- countAndSay(3) = "21" (two 1s)
- countAndSay(4) = "1211" (one 2, one 1)

---

💡 Core Idea:
Start from "1" and iteratively build the sequence up to n using RLE.
Each iteration, read the current string and construct the next by counting consecutive characters.

👉 Can be implemented both recursively and iteratively. Iterative is more efficient and avoids call stack depth issues.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        
        for _ in range(1, n):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive same characters
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                current += str(count) + result[i]
                i += 1
            result = current
        
        return result


# -------------------------
# 🔸 Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))  # "1"
    print(sol.countAndSay(4))  # "1211"
    print(sol.countAndSay(5))  # "111221"
    print(sol.countAndSay(6))  # "312211"

"""
⏱ Time Complexity: O(n * m)
    - Where n is the input and m is the average length of the string during each iteration.
    - Worst-case exponential growth of string length with each level.

💾 Space Complexity: O(m)
    - Only one string stored and updated per level.
"""
