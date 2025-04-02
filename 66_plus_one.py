"""
🔵 LeetCode 66: Plus One

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit 
of the integer. The digits are ordered from most significant to least significant in left-to-right order. The 
large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

-----------------------------------
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10.

-----------------------------------

Constraints:
    - 1 <= digits.length <= 100
    - 0 <= digits[i] <= 9
    - `digits` does not contain any leading 0's.
"""

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    """
    This function increments the large integer represented by the list of digits by one.
    
    Approach:
      - Start from the least significant digit (the end of the list) and add one.
      - Propagate the carry if the sum of the digit and the carry equals 10.
      - If a carry remains after processing all digits, insert it at the beginning of the list.
    
    Time Complexity: O(n), where n is the number of digits.
    Space Complexity: O(1) (in-place modification, aside from the potential insertion at the front).
    
    Args:
        digits (List[int]): A list of integers representing the large integer.
        
    Returns:
        List[int]: The resulting list of digits after incrementing by one.
    """
    n = len(digits)
    carry = 1  # Start by adding one
    
    # Process the digits from right to left.
    for i in range(n - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10  # Update the current digit
        carry = total // 10     # Calculate new carry
        if carry == 0:
            break  # No further carry, we can exit early
            
    # If carry remains, insert it at the front.
    if carry:
        digits.insert(0, carry)
        
    return digits

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    digits1 = [1, 2, 3]
    print("Example 1 Output:", plusOne(digits1))  # Expected: [1, 2, 4]
    
    # Example 2:
    digits2 = [4, 3, 2, 1]
    print("Example 2 Output:", plusOne(digits2))  # Expected: [4, 3, 2, 2]
    
    # Example 3:
    digits3 = [9]
    print("Example 3 Output:", plusOne(digits3))  # Expected: [1, 0]

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of digits.
# ✅ Space Complexity: O(1), aside from the in-place modification and potential insertion at the front.
