"""
🔷 LeetCode 118 – Pascal's Triangle

🧠 Problem Summary:
Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

✅ Constraints:
- 1 <= numRows <= 30

---

📌 Example:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]

---

💡 Core Idea:
Each row starts and ends with 1.
For elements in between, they are the sum of the two values above from the previous row.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for row_num in range(numRows):
            # Start with a row of 1s
            row = [1] * (row_num + 1)

            # Fill the middle values using previous row
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


# -------------------------
# 🔸 Example test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(sol.generate(1))  # [[1]]

"""
⏱ Time Complexity: O(numRows^2)
    - Each row has up to `numRows` elements.
    - Filling each value takes constant time.

💾 Space Complexity: O(numRows^2)
    - Triangle list stores all rows explicitly.
"""
