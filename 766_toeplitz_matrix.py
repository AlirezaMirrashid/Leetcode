"""
🔷 LeetCode 766 – Toeplitz Matrix

🧠 Problem Summary:
Given an m x n matrix, return True if the matrix is Toeplitz.  
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

📌 Examples:

Example 1:
Input:
    matrix = [
      [1, 2, 3, 4],
      [5, 1, 2, 3],
      [9, 5, 1, 2]
    ]
Output: True

Example 2:
Input:
    matrix = [
      [1, 2],
      [2, 2]
    ]
Output: False

📋 Constraints:
    m == matrix.length  
    n == matrix[i].length  
    1 <= m, n <= 20  
    0 <= matrix[i][j] <= 99  

🔄 Follow-up:
1. If you can load only one row at a time into memory.
2. If you can load only part of a row at a time (streaming/chunked).

---

Solution approaches below:
"""

from typing import List, Iterator

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Basic in-memory check:
        Iterate through all cells except the last row and last column,
        and verify each equals its down-right neighbor.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

    def isToeplitzMatrix_row_by_row(self, row_iter: Iterator[List[int]]) -> bool:
        """
        Follow-up 1: Only one row in memory at a time.
        We keep the previous row, and as we read the current row,
        we check prev_row[j] == curr_row[j+1] for j in [0..n-2].
        Then discard prev_row, shift current to prev_row.
        """
        prev = next(row_iter, None)
        if prev is None:
            return True
        n = len(prev)
        for curr in row_iter:
            # check diagonal consistency between prev and curr
            for j in range(n - 1):
                if prev[j] != curr[j + 1]:
                    return False
            prev = curr
        return True

    def isToeplitzMatrix_chunked(self,
                                 row_chunks_iter: Iterator[List[int]],
                                 chunk_size: int) -> bool:
        """
        Follow-up 2: Rows arrive in chunks of length `chunk_size`.
        We stream through each chunk but only need to remember
        the last element of the previous chunk to compare diagonally
        into the next row's first chunk, and within a row chunk we
        compare adjacent elements across chunk boundaries.

        We assume row_chunks_iter yields chunks in row-major order:
          first all chunks of row0, then all chunks of row1, etc.

        Each yielded chunk is a tuple (row_index, chunk_index, chunk_list).
        """
        prev_row_last_elems = []  # will hold the tail elements of the previous row
        current_row = -1
        chunk_index = 0

        for row_index, ch_idx, chunk in row_chunks_iter:
            if row_index != current_row:
                # starting new row
                prev_row_last_elems = curr_row_chunks  # rename from last iteration
                curr_row_chunks = []                   # reset for this row
                current_row = row_index
                chunk_index = 0

            # within the same row, for chunk 0..k
            # compare this chunk with prev_row_last_elems if not first row
            if row_index > 0:
                # for each element in this chunk at local pos j,
                # it should match prev_row_last_elems[j+chunk_offset]
                offset = chunk_size * ch_idx
                for j, val in enumerate(chunk):
                    # diagonal from prev row: at index offset+j+1
                    diag_idx = offset + j + 1
                    # only compare if diag_idx falls within prev row length
                    if diag_idx < len(prev_row_last_elems):
                        if val != prev_row_last_elems[diag_idx]:
                            return False

            # keep this chunk to form next row's prev_row_last_elems
            curr_row_chunks.extend(chunk)
            chunk_index += 1

        return True


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    print(sol.isToeplitzMatrix(matrix1))  # True

    matrix2 = [
        [1, 2],
        [2, 2]
    ]
    print(sol.isToeplitzMatrix(matrix2))  # False

    # follow-up #1: simulate row-by-row streaming
    def row_stream():
        for row in matrix1:
            yield row

    print(sol.isToeplitzMatrix_row_by_row(row_stream()))  # True

    # follow-up #2: simulate chunked streaming
    # e.g. chunk_size = 2
    def chunked_stream(matrix, chunk_size):
        for i, row in enumerate(matrix):
            for ci in range(0, len(row), chunk_size):
                yield (i, ci // chunk_size, row[ci:ci+chunk_size])

    print(sol.isToeplitzMatrix_chunked(chunked_stream(matrix1, 2), 2))  # True


"""
⏱ Time Complexity:
 - Basic: O(m·n)
 - Row-by-row: O(m·n)
 - Chunked: O(m·n)

💾 Space Complexity:
 - Basic: O(1) extra
 - Row-by-row: O(n) to store one row
 - Chunked: O(chunk_size) to store one chunk plus O(n) to assemble row tails (can be O(1) if only tails are kept)
"""
