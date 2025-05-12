"""
🔵 LeetCode 63. Unique Paths II

You are given an `m x n` integer array `obstacleGrid`. A robot is initially located at the top-left corner (i.e., `obstacleGrid[0][0]`), and it can only move **right** or **down**.

An obstacle is marked as `1` and free space as `0`. The robot cannot step on obstacles.

Return the number of unique paths the robot can take to reach the bottom-right corner (i.e., `obstacleGrid[m-1][n-1]`), avoiding all obstacles.

-----------------------------------
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: Two possible paths:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

-----------------------------------
Constraints:
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is either 0 or 1
"""

from typing import List

def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    """
    ✅ Optimal DP Solution (Bottom-Up)

    Idea:
    - Use dynamic programming to store the number of ways to reach each cell.
    - If the cell is an obstacle, set its paths to 0.
    - Otherwise, sum the paths from the top and left cells.

    Time Complexity: O(m * n)
    Space Complexity: O(1) (in-place DP)
    """
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0

    grid[0][0] = 1

    # Fill first column
    for i in range(1, m):
        grid[i][0] = 0 if grid[i][0] == 1 else grid[i - 1][0]

    # Fill first row
    for j in range(1, n):
        grid[0][j] = 0 if grid[0][j] == 1 else grid[0][j - 1]

    # Fill rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[m - 1][n - 1]


def unique_paths_with_obstacles_brute(grid: List[List[int]]) -> int:
    """
    ❌ Brute Force (DFS with Memoization - Still not optimal for large grids)

    Idea:
    - Explore all possible paths using recursion.
    - Use memoization to cache results for subproblems.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n) for recursion and memo
    """
    from functools import lru_cache
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dfs(r: int, c: int) -> int:
        if r >= m or c >= n or grid[r][c] == 1:
            return 0
        if r == m - 1 and c == n - 1:
            return 1
        return dfs(r + 1, c) + dfs(r, c + 1)

    return dfs(0, 0)


# ✅ Sample Test Cases
if __name__ == "__main__":
    grid1 = [[0,0,0],[0,1,0],[0,0,0]]
    print("Optimal:", unique_paths_with_obstacles([row[:] for row in grid1]))  # 2
    print("Brute Force:", unique_paths_with_obstacles_brute(tuple(map(tuple, grid1))))  # 2

    grid2 = [[0,1],[0,0]]
    print("Optimal:", unique_paths_with_obstacles([row[:] for row in grid2]))  # 1
    print("Brute Force:", unique_paths_with_obstacles_brute(tuple(map(tuple, grid2))))  # 1

    grid3 = [[1]]
    print("Optimal:", unique_paths_with_obstacles([row[:] for row in grid3]))  # 0
    print("Brute Force:", unique_paths_with_obstacles_brute(tuple(map(tuple, grid3))))  # 0
