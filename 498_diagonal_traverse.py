"""
🔷 LeetCode 498 - Diagonal Traverse

🧠 Task:
Given an m x n matrix `mat`, return an array of all the elements of the matrix in a diagonal order.

Diagonal order means starting at (0,0), then moving up-right until boundary, then down-left, alternating directions.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- -10^5 <= mat[i][j] <= 10^5
"""
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        ✅ Optimal Approach: Simulate traversal by tracking direction and boundaries

        We iterate over total m*n elements, maintaining current (r, c) and direction:
        - If moving up-right (dir = 1): r--, c++
        - If moving down-left (dir = -1): r++, c--
        Whenever we go out of bounds, we adjust r,c to next valid start and flip direction.

        Time Complexity: O(m*n)
        Space Complexity: O(1) extra (output list not counted)
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        r = c = 0
        dir = 1  # 1 = up-right, -1 = down-left
        for _ in range(m * n):
            result.append(mat[r][c])
            # move in current direction
            nr, nc = r + (-1 if dir == 1 else 1), c + (1 if dir == 1 else -1)
            # if out of bounds, compute next start
            if nr < 0 or nr == m or nc < 0 or nc == n:
                if dir == 1:
                    # previous move was up-right
                    if c + 1 < n:
                        r, c = r, c + 1
                    else:
                        r, c = r + 1, c
                else:
                    # previous move was down-left
                    if r + 1 < m:
                        r, c = r + 1, c
                    else:
                        r, c = r, c + 1
                dir *= -1
            else:
                r, c = nr, nc
        return result

    def findDiagonalOrderGroup(self, mat: List[List[int]]) -> List[int]:
        """
        ✅ Alternative: Group by (r+c) diagonals then flatten with direction flip

        Use a dictionary grouping values by key = r+c. For each diagonal key,
        if key is even, reverse group before adding; if odd, keep order.

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        from collections import defaultdict
        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[i+j].append(mat[i][j])
        result = []
        for k in range(m+n-1):
            diag = groups[k]
            if k % 2 == 0:
                result.extend(reversed(diag))
            else:
                result.extend(diag)
        return result

    def findDiagonalOrderBruteForce(self, mat: List[List[int]]) -> List[int]:
        """
        ❌ Brute Force: Generate all coordinates in traversal order via sorting

        Construct list of (order_index, value), where order_index increases along diagonals,
        then sort by (r+c, and within same diagonal by r or c depending on direction),
        then extract values. Complexity O(m*n*log(m*n)).

        Time Complexity: O(m*n*log(m*n))
        Space Complexity: O(m*n)
        """
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        entries = []
        for i in range(m):
            for j in range(n):
                d = i + j
                # for even diagonals, we want r descending, so use -i
                order_in_diag = -i if d % 2 == 0 else i
                entries.append((d, order_in_diag, mat[i][j]))
        entries.sort()
        return [val for _, _, val in entries]

# Quick test
def main():
    sol = Solution()
    mat1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.findDiagonalOrder(mat1))       # [1,2,4,7,5,3,6,8,9]
    print(sol.findDiagonalOrderGroup(mat1))  # same
    print(sol.findDiagonalOrderBruteForce(mat1))

    mat2 = [[1,2],[3,4]]
    print(sol.findDiagonalOrder(mat2))       # [1,2,3,4]

if __name__ == '__main__':
    main()
