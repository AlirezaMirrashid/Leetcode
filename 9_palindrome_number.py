"""
🔵 LeetCode 9: Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

A palindrome number is a number that remains the same when its digits are reversed.
Note: Negative numbers are not considered palindromes.

-----------------------------------
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-, which is not the same.

Example 3:
Input: x = 10
Output: false
Explanation: Reads as 01 from right to left, hence it is not a palindrome.

-----------------------------------
Constraints:
    - -2^31 <= x <= 2^31 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

def isPalindrome(x: int) -> bool:
    """
    Optimal solution by reversing the integer.
    
    Approach:
      - Negative numbers are not palindromes.
      - Reverse the integer by extracting its digits.
      - Compare the reversed number with the original number.
    

    Args:
        x (int): The input integer.
    
    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    if x < 0:
        return False
    
    original = x
    reversed_num = 0
    while x:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return reversed_num == original

def isPalindrome_alternative(x: int) -> bool:
    """
    Alternative solution without converting the integer to a string by comparing digits from both ends.
    
    Approach:
      - Negative numbers are not palindromes.
      - Determine the divisor to extract the leftmost digit.
      - Compare the leftmost and rightmost digits.
      - Remove the leftmost and rightmost digits from x and adjust the divisor.
      - Continue until all digits are processed.

    
    Args:
        x (int): The input integer.
    
    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    if x < 0:
        return False

    div = 1
    # Find the divisor to extract the leftmost digit
    while x >= 10 * div:
        div *= 10

    while x:
        right = x % 10          # Rightmost digit
        left = x // div         # Leftmost digit
        
        if left != right:
            return False
        
        # Remove leftmost and rightmost digits
        x = (x % div) // 10
        div //= 100  # Two digits are removed, adjust the divisor accordingly

    return True

# Sample Test Cases
if __name__ == "__main__":
    # Using the reverse method
    print(isPalindrome(121))    # Expected: True
    print(isPalindrome(-121))   # Expected: False
    print(isPalindrome(10))     # Expected: False
    print(isPalindrome(0))      # Expected: True
    
    # Using the alternative method
    print(isPalindrome_alternative(121))    # Expected: True
    print(isPalindrome_alternative(-121))   # Expected: False
    print(isPalindrome_alternative(10))     # Expected: False
    print(isPalindrome_alternative(0))      # Expected: True

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of digits in the input integer.
# ✅ Space Complexity: O(1), as only a constant amount of extra space is used.
