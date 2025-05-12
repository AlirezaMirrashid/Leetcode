"""
🔷 LeetCode 695: Max Area of Island (Medium)

You are given an m × n binary matrix `grid`. An island is a group of `1`’s (land) connected 4-directionally (horizontal or vertical). 
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value `1` in that island.  
Return the maximum area of an island in `grid`. If there is no island, return `0`.

Example 1:
    Input:
        grid = [
          [0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
    Output: 6

Example 2:
    Input:
        grid = [[0,0,0,0,0,0,0,0]]
    Output: 0

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""

from collections import deque
from copy import deepcopy
from typing import List

def maxAreaOfIsland_dfs(grid: List[List[int]]) -> int:
    """
    DFS approach.
    """
    m, n = len(grid), len(grid[0])
    seen = [[False]*n for _ in range(m)]
    
    def dfs(i: int, j: int) -> int:
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or seen[i][j]:
            return 0
        seen[i][j] = True
        area = 1
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            area += dfs(i+di, j+dj)
        return area

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not seen[i][j]:
                max_area = max(max_area, dfs(i, j))
    return max_area

def maxAreaOfIsland_bfs(grid: List[List[int]]) -> int:
    """
    BFS approach.
    """
    m, n = len(grid), len(grid[0])
    seen = [[False]*n for _ in range(m)]
    max_area = 0

    for si in range(m):
        for sj in range(n):
            if grid[si][sj] == 1 and not seen[si][sj]:
                area = 0
                q = deque([(si, sj)])
                seen[si][sj] = True
                while q:
                    i, j = q.popleft()
                    area += 1
                    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and not seen[ni][nj]:
                            seen[ni][nj] = True
                            q.append((ni, nj))
                max_area = max(max_area, area)
    return max_area

def maxAreaOfIsland_bruteforce(grid: List[List[int]]) -> int:
    """
    Brute-force: for each land cell, deep-copy grid and flood-fill.
    """
    m, n = len(grid), len(grid[0])
    max_area = 0

    def flood_fill(g: List[List[int]], i: int, j: int) -> int:
        if i<0 or i>=m or j<0 or j>=n or g[i][j] == 0:
            return 0
        g[i][j] = 0
        area = 1
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            area += flood_fill(g, i+di, j+dj)
        return area

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                gcopy = deepcopy(grid)
                area = flood_fill(gcopy, i, j)
                max_area = max(max_area, area)
    return max_area

if __name__ == "__main__":
    # sample test runs
    tests = [
        (
            [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ],
            6
        ),
        ([[0,0,0,0,0,0,0,0]], 0),
    ]
    for grid, expected in tests:
        print("DFS   ->", maxAreaOfIsland_dfs(grid), "expected", expected)
        print("BFS   ->", maxAreaOfIsland_bfs(grid), "expected", expected)
        print("Brute ->", maxAreaOfIsland_bruteforce(grid), "expected", expected)
        print("---")

# Complexity
# DFS:
#   Time:  O(m * n)
#   Space: O(m * n)   (recursion stack + visited array)
#
# BFS:
#   Time:  O(m * n)
#   Space: O(m * n)   (queue + visited array)
#
# Brute-force:
#   Time:  O((m * n)²)
#   Space: O(m * n)   (grid copy + recursion stack)
