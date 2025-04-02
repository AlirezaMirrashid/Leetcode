"""
🔵 LeetCode 1757: Recyclable and Low Fat Products

You are given a table `Products` with the following columns:
    - product_id (int): The unique identifier for the product.
    - low_fats (enum): 'Y' if the product is low fat, 'N' otherwise.
    - recyclable (enum): 'Y' if the product is recyclable, 'N' otherwise.

Write a query to find the ids of products that are both low fat and recyclable.

-----------------------------------
Example 1:
Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation:
    Only products with product_id 1 and 3 are both low fat and recyclable.
-----------------------------------

SQL Query:
"""
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';
