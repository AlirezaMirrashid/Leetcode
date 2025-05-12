"""
🔷 LeetCode 200: Number of Islands

Given an m × n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), 
return the **number of islands**.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input:
        grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
    Output: 1

Example 2:
    Input:
        grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
    Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 ≤ m, n ≤ 300
    grid[i][j] is '0' or '1'.
"""

from collections import deque
from typing import List

# 1) DFS approach
def numIslands_dfs(grid: List[List[str]]) -> int:
    """
    Use DFS to mark all connected land from each unvisited '1'.
    Time: O(m·n), Space: O(m·n) recursion stack + visited.
    """
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]

    def dfs(i: int, j: int):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1' or visited[i][j]:
            return
        visited[i][j] = True
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                dfs(i, j)
    return count

# 2) BFS approach
def numIslands_bfs(grid: List[List[str]]) -> int:
    """
    Use BFS to traverse each discovered island.
    Time: O(m·n), Space: O(m·n) queue + visited.
    """
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    count = 0

    for si in range(m):
        for sj in range(n):
            if grid[si][sj] == '1' and not visited[si][sj]:
                count += 1
                q = deque([(si, sj)])
                visited[si][sj] = True
                while q:
                    i, j = q.popleft()
                    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1' and not visited[ni][nj]:
                            visited[ni][nj] = True
                            q.append((ni, nj))
    return count

# 3) Union-Find approach
class UnionFind:
    def __init__(self, grid: List[List[str]]):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i*n + j
                    self.parent[idx] = idx
                    self.count += 1

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            # union by rank
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1
            self.count -= 1

def numIslands_union_find(grid: List[List[str]]) -> int:
    """
    Use Union-Find to merge adjacent lands.
    Time: O(m·n·α(mn)), Space: O(m·n).
    """
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    uf = UnionFind(grid)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                idx = i*n + j
                # union right and down to avoid duplicates
                for di, dj in [(1,0),(0,1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        uf.union(idx, ni*n + nj)
    return uf.count

# ------------- Sample tests -------------
if __name__ == "__main__":
    tests = [
        (
            [
              ["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ],
            3
        ),
    ]
    for grid, expected in tests:
        print("DFS          ->", numIslands_dfs(grid),           "expected", expected)
        print("BFS          ->", numIslands_bfs(grid),           "expected", expected)
        print("Union-Find   ->", numIslands_union_find(grid),    "expected", expected)
        print("---")

# Complexity Summary:
# DFS:
#   Time:  O(m·n)
#   Space: O(m·n)   (recursion stack + visited array)
# BFS:
#   Time:  O(m·n)
#   Space: O(m·n)   (queue + visited array)
# Union-Find:
#   Time:  O(m·n·α(mn)) ≈ O(m·n)
#   Space: O(m·n)   (parent + rank arrays)
