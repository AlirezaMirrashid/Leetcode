"""
🔷 LeetCode 48 – Rotate Image

🧠 Problem Summary:
Given an n×n 2D matrix representing an image, rotate the image by 90 degrees clockwise in-place.
You must modify the input matrix directly without allocating another 2D matrix.

✅ Constraints:
- n == matrix.length == matrix[i].length
- 1 ≤ n ≤ 20
- -1000 ≤ matrix[i][j] ≤ 1000

---

📌 Examples:

Example 1:
Input:
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
After calling rotate(matrix), matrix becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Input:
matrix = [
  [5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]
]
After calling rotate(matrix), matrix becomes:
[
  [15,13,2,5],
  [14,3,4,1],
  [12,6,8,9],
  [16,7,10,11]
]

---

💡 Core Idea (Method 1: Transpose + Reverse Rows):
1. **Transpose** the matrix (swap matrix[i][j] with matrix[j][i]).
2. **Reverse each row** to achieve the 90° clockwise rotation.

---

💡 Core Idea (Method 2: Layer-by-Layer Four-Way Swap):
Process the matrix in layers from the outermost to the innermost. For each layer, perform a four-way swap for each element in the layer:
- top → right → bottom → left → top

---

🐍 Python Implementation:
"""
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Method 1: Transpose + Reverse Rows
        
        ⏱ Time Complexity: O(n²)
        💾 Space Complexity: O(1)
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()

    def rotate_layer(self, matrix: list[list[int]]) -> None:
        """
        Method 2: Layer-by-Layer Four-Way Swap
        
        ⏱ Time Complexity: O(n²)
        💾 Space Complexity: O(1)
        """
        n = len(matrix)
        # Process layers
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                # save top
                top = matrix[first][i]
                # left -> top
                matrix[first][i] = matrix[last - offset][first]
                # bottom -> left
                matrix[last - offset][first] = matrix[last][last - offset]
                # right -> bottom
                matrix[last][last - offset] = matrix[i][last]
                # top -> right
                matrix[i][last] = top


# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    
    mat1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    # using transpose+reverse
    sol.rotate(mat1)
    print("Transpose+Reverse:", mat1)  # [[7,4,1],[8,5,2],[9,6,3]]
    
    mat2 = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]
    # using layer-by-layer
    sol.rotate_layer(mat2)
    print("Layer-by-Layer:", mat2)
    # [[15,13,2,5],
    #  [14,3,4,1],
    #  [12,6,8,9],
    #  [16,7,10,11]]
