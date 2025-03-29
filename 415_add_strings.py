"""
🔵 LeetCode 415: Add Strings

Given two non-negative integers, num1 and num2 represented as strings, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger) 
and without converting the inputs to integers directly.

-----------------------------------
Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

-----------------------------------
Constraints:
    - 1 <= num1.length, num2.length <= 10^4
    - num1 and num2 consist of only digits.
    - num1 and num2 don't have any leading zeros except for the zero itself.
"""

def add_strings(num1: str, num2: str) -> str:
    """
    Adds two non-negative integers represented as strings without converting them directly to integers.

    Approach:
    - Process the strings from right (least-significant digit) to left.
    - Add corresponding digits along with the carry from previous additions.
    - Append the result digit to a list and update the carry.
    - After processing all digits, if a carry remains, append it.
    - Reverse and join the result list to form the final sum string.

    Parameters:
        num1 (str): The first non-negative integer as a string.
        num2 (str): The second non-negative integer as a string.
    
    Returns:
        str: The sum of num1 and num2 represented as a string.
    """
    i, j = len(num1) - 1, len(num2) - 1  # Pointers for num1 and num2
    carry = 0  # Initialize carry
    result = []  # List to store result digits
    
    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        # Compute sum of digits and carry
        total = digit1 + digit2 + carry
        carry = total // 10  # Update carry
        result.append(str(total % 10))  # Append current digit
        
        i -= 1
        j -= 1

    # The result list is in reverse order, so reverse it to get the final string.
    return ''.join(result[::-1])


# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    num1_ex1 = "11"
    num2_ex1 = "123"
    print("Example 1 Output:", add_strings(num1_ex1, num2_ex1))  # Expected: "134"

    # Example 2:
    num1_ex2 = "456"
    num2_ex2 = "77"
    print("Example 2 Output:", add_strings(num1_ex2, num2_ex2))  # Expected: "533"

    # Example 3:
    num1_ex3 = "0"
    num2_ex3 = "0"
    print("Example 3 Output:", add_strings(num1_ex3, num2_ex3))  # Expected: "0"

# ------------------------------------------------
# ✅ Time Complexity: O(max(n, m)) or O(n+m)
# ✅ Space Complexity: O(max(n, m)) or O(n+m)
#   where n = len(num1) and m = len(num2)
