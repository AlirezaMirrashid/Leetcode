"""
🔷 LeetCode 827 - Making A Large Island

🧠 Task:
You are given an n x n binary matrix `grid`. You may change at most one 0 to 1.
Return the size of the largest island after this operation. An island is a 4-directionally connected group of 1s.

-----------------------------------
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 to connect two islands of size 1 → size 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Flip the 0 to 1 → single island size 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: No zeros to flip; largest island is 4.

Constraints:
  - n == grid.length == grid[i].length
  - 1 <= n <= 500
  - grid[i][j] is 0 or 1.
"""

from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        ✅ Optimal Two-Pass with Component Labeling

        1) First pass: flood-fill each island of 1s with a unique id (starting from 2)
           and record its area in a map `area[id]`.
        2) Second pass: for each 0 cell, look at its 4-directional neighbors,
           collect distinct island ids, sum their areas + 1 (for the flipped cell),
           track the maximum.
        Also handle the case of no zero in grid (max area unchanged).

        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        (n x n grid)
        """
        n = len(grid)
        area = {}  # island_id -> area
        island_id = 2
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # Flood-fill to label islands and compute area
        def bfs_mark(i, j, id):
            q = deque([(i,j)])
            grid[i][j] = id
            a = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        a += 1
                        q.append((nx, ny))
            return a

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[island_id] = bfs_mark(i, j, island_id)
                    island_id += 1

        # If no zero was found, entire grid might be one island
        max_area = max(area.values(), default=0)

        # Try flipping each zero
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    a = 1
                    for dx, dy in directions:
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < n and 0 <= nj < n:
                            id = grid[ni][nj]
                            if id > 1 and id not in seen:
                                seen.add(id)
                                a += area[id]
                    max_area = max(max_area, a)
        return max_area

    def largestIslandBruteForce(self, grid: List[List[int]]) -> int:
        """
        ❌ Brute Force: For each 0, flip it, BFS to compute largest island area, then revert.

        Time Complexity: O((n^2) * n^2) = O(n^4) worst-case
        Space Complexity: O(n^2)
        """
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs_area(i, j):
            q = deque([(i,j)])
            seen = {(i,j)}
            a = 1
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in seen and grid[nx][ny] == 1:
                        seen.add((nx,ny))
                        a += 1
                        q.append((nx, ny))
            return a

        max_area = 0
        # compute baseline
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs_area(i, j))
        # try flips
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    max_area = max(max_area, bfs_area(i, j))
                    grid[i][j] = 0
        return max_area

# 🔸 Sample Test
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1,0],[0,1]]
    print(sol.largestIsland(grid1))  # 3
    grid2 = [[1,1],[1,0]]
    print(sol.largestIsland(grid2))  # 4
    grid3 = [[1,1],[1,1]]
    print(sol.largestIsland(grid3))  # 4

    # Brute-force for small n
    grid4 = [[1,0,1],[0,1,0],[1,0,1]]
    print(sol.largestIslandBruteForce(grid4))  # 5
