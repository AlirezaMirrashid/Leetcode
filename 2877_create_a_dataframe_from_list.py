"""
🔵 LeetCode 2877: Create a DataFrame from List

Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages 
of some students. The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

-----------------------------------
Example 1:
Input:
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
-----------------------------------

Constraints:
    - The 2D list will contain valid student IDs and ages.
"""

import pandas as pd
from typing import List

def createStudentDataFrame(student_data: List[List[int]]) -> pd.DataFrame:
    """
    Creates a Pandas DataFrame from a 2D list `student_data` with columns 'student_id' and 'age'.
    
    Approach:
      - Use the pd.DataFrame constructor with the provided list and specify the column names.
    
    Time Complexity: O(n), where n is the number of rows in student_data.
    Space Complexity: O(n), as the DataFrame stores the data from the input list.
    
    Args:
        student_data (List[List[int]]): A 2D list containing student IDs and ages.
    
    Returns:
        pd.DataFrame: A DataFrame with columns 'student_id' and 'age', preserving the order of student_data.
    """
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Sample Test Cases
if __name__ == "__main__":
    student_data = [
        [1, 15],
        [2, 11],
        [3, 11],
        [4, 20]
    ]
    df = createStudentDataFrame(student_data)
    print(df)
    
# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of rows in student_data.
# ✅ Space Complexity: O(n), as the DataFrame stores the data from the input list.
