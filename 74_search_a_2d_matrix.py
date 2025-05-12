"""
🔷 LeetCode 74 – Search a 2D Matrix

🧠 Problem Summary:
Given an m x n matrix where each row is sorted, and the first element of each row is greater than the last of the previous row,
determine if a target value exists in the matrix.

✅ Constraints:
- Time complexity must be O(log(m * n))

---

📌 Example:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: False

---

💡 Solution 1 (Flattened binary search):
Treat the matrix as a flattened sorted array and binary search over it.
Map 1D index → 2D row, col.

💡 Solution 2 (Two-stage binary search):
1. Binary search to find the candidate row.
2. Binary search inside that row to find the target.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        # Flattened binary search
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrixTwoBinarySearch(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        
        # Binary search over rows to find candidate row
        top, bottom = 0, m - 1
        row = -1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
                row = mid_row
                break
            elif matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        if row == -1:
            return False

        # Binary search within the row
        left, right = 0, n - 1
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1

        return False


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(sol.searchMatrix(matrix1, 3))                 # True
    print(sol.searchMatrix(matrix1, 13))               # False
    print(sol.searchMatrixTwoBinarySearch(matrix1, 3))  # True
    print(sol.searchMatrixTwoBinarySearch(matrix1, 13)) # False

"""
⏱ Time Complexity:
- Flattened binary search: O(log(m * n))
- Two binary searches: O(log m + log n)

💾 Space Complexity:
- Both solutions: O(1)
"""
