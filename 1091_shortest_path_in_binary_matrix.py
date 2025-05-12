"""
🔷 LeetCode 1091: Shortest Path in Binary Matrix (Medium)

🧠 Task:
Given an n x n binary matrix `grid`, return the length of the shortest clear path in the matrix.
A clear path is defined as a path from the top-left cell (0,0) to the bottom-right cell (n-1,n-1)
where:
  - Every visited cell is 0.
  - Every adjacent cell in the path is 8-directionally connected.
The length of the path is the number of visited cells. If there is no clear path, return -1.

-----------------------------------
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

-----------------------------------
Constraints:
    - n == grid.length and n == grid[i].length
    - 1 <= n <= 100
    - grid[i][j] is 0 or 1
"""

from typing import List
from collections import deque
import heapq  # For the alternative (A* search) approach if needed

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        ✅ Optimal BFS Approach
        
        Approach:
          - Use Breadth-First Search (BFS) starting from (0,0) if it's clear (0). 
          - Explore 8-directional moves from each cell.
          - Maintain a visited set or mark the grid to avoid re-processing cells.
          - When reaching the bottom-right cell, return the number of steps.
          - Return -1 if no path is found.
        
        ⏱ Time Complexity: O(n^2) in the worst-case, where n is the side length of the grid.
        💾 Space Complexity: O(n^2) due to the queue in the worst-case.
        
        Args:
            grid (List[List[int]]): An n x n binary matrix.
        
        Returns:
            int: The length of the shortest clear path, or -1 if no such path exists.
        """
        n = len(grid)
        # Check if start or end is blocked.
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # All 8 possible moves (including diagonals)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]
        
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited using grid modification
        
        while queue:
            row, col, path = queue.popleft()
            if row == n - 1 and col == n - 1:
                return path
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    grid[r][c] = 1  # Mark as visited
                    queue.append((r, c, path + 1))
        return -1

    # def shortestPathBinaryMatrixAStar(self, grid: List[List[int]]) -> int:
    #     """
    #     ✅ Alternative A* Search Approach

    #     Approach:
    #       - Use A* search to guide the BFS with a heuristic (Chebyshev distance) 
    #         since movement is 8-directional.
    #       - The heuristic estimates the remaining steps to the target.
    #       - This method may perform faster on some grids but has a worst-case complexity similar to BFS.

    #     ⏱ Time Complexity: O(n^2) in the worst case.
    #     💾 Space Complexity: O(n^2)
        
    #     Args:
    #         grid (List[List[int]]): An n x n binary matrix.
        
    #     Returns:
    #         int: The length of the shortest clear path, or -1 if no path exists.
    #     """
    #     n = len(grid)
    #     if grid[0][0] or grid[n-1][n-1]:
    #         return -1

    #     # Heuristic function: Chebyshev distance
    #     def heuristic(r: int, c: int) -> int:
    #         return max(n - 1 - r, n - 1 - c)

    #     # Use a min-heap as the priority queue.
    #     heap = [(1 + heuristic(0, 0), 0, 0, 1)]  # (estimated_cost, row, col, path_length)
    #     visited = {(0, 0)}
    #     directions = [(-1, -1), (-1, 0), (-1, 1),
    #                   (0, -1),          (0, 1),
    #                   (1, -1), (1, 0),  (1, 1)]

    #     while heap:
    #         est, row, col, path = heapq.heappop(heap)
    #         if row == n - 1 and col == n - 1:
    #             return path
    #         for dr, dc in directions:
    #             r, c = row + dr, col + dc
    #             if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 and (r, c) not in visited:
    #                 visited.add((r, c))
    #                 heapq.heappush(heap, (path + 1 + heuristic(r, c), r, c, path + 1))
    #     return -1

# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1:
    grid1 = [[0,1],[1,0]]
    print("Example 1 Output (BFS):", sol.shortestPathBinaryMatrix([row[:] for row in grid1]))   # Expected: 2
    # print("Example 1 Output (A*):", sol.shortestPathBinaryMatrixAStar([row[:] for row in grid1]))   # Expected: 2

    # Example 2:
    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    print("Example 2 Output (BFS):", sol.shortestPathBinaryMatrix([row[:] for row in grid2]))   # Expected: 4
    # print("Example 2 Output (A*):", sol.shortestPathBinaryMatrixAStar([row[:] for row in grid2]))   # Expected: 4

    # Example 3:
    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    print("Example 3 Output (BFS):", sol.shortestPathBinaryMatrix([row[:] for row in grid3]))   # Expected: -1
    # print("Example 3 Output (A*):", sol.shortestPathBinaryMatrixAStar([row[:] for row in grid3]))   # Expected: -1

# ------------------------------------------------
# ✅ BFS Approach:
#      Time Complexity: O(n^2) worst-case.
#      Space Complexity: O(n^2) worst-case.
#
# ✅ A* Search Approach:
#      Time Complexity: O(n^2) worst-case, though typically faster with a good heuristic.
#      Space Complexity: O(n^2)
