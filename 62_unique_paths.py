"""
🔵 LeetCode 62. Unique Paths

A robot is located at the top-left corner of an m x n grid.
The robot can only move either down or right at any point in time.
Return the number of unique paths to reach the bottom-right corner (m-1, n-1).

-----------------------------------
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: 
- Right -> Down -> Down
- Down -> Down -> Right
- Down -> Right -> Down

-----------------------------------
Constraints:
- 1 <= m, n <= 100
"""

def unique_paths(m: int, n: int) -> int:
    """
    ✅ Dynamic Programming (Tabulation)

    Idea:
    - Create a 2D dp array where dp[i][j] = number of ways to reach cell (i, j).
    - The first row and first column can only be reached in one way.
    - For each cell, the number of ways = dp[i-1][j] (top) + dp[i][j-1] (left)

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    dp = [[1] * n for _ in range(m)]  # initialize with 1s

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


# ✅ Sample Test Cases
if __name__ == "__main__":
    print(unique_paths(3, 7))  # Output: 28
    print(unique_paths(3, 2))  # Output: 3
    print(unique_paths(1, 1))  # Output: 1
    print(unique_paths(10, 10))  # Output: 48620
