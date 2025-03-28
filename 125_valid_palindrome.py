# LeetCode 125: Valid Palindrome
# Problem Link: https://leetcode.com/problems/valid-palindrome/
#
# Description:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: The string is empty after cleaning and reads the same forward and backward.
#
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

import re

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a valid palindrome after removing non-alphanumeric characters
    and converting it to lowercase.

    This solution uses two pointers to efficiently check for a palindrome.

    Parameters:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # # Filter alphanumeric characters and convert to lowercase
    # cleaned_s = [char.lower() for char in s if char.isalnum()]

    # Use two pointers to check if it's a palindrome
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right < left and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# def isalnum(c):
#     return (ord('A') <= ord(c) <= ord('Z') or 
#             ord('a') <= ord(c) <= ord('z') or
#             ord('0') <= ord(c) <= ord('9'))

# Brute-force Alternative:
def is_palindrome_brute_force(s: str) -> bool:
    """
    Brute-force approach to check if a string is a palindrome.

    This method first cleans the string using regular expressions and then
    compares the cleaned string with its reverse.

    Parameters:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Compare the string with its reverse
    return cleaned_s == cleaned_s[::-1]


# Example test cases:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected output: True
print(is_palindrome("race a car"))  # Expected output: False
print(is_palindrome(" "))  # Expected output: True

# Testing the brute-force alternative:
print(is_palindrome_brute_force("A man, a plan, a canal: Panama"))  # Expected output: True
print(is_palindrome_brute_force("race a car"))  # Expected output: False
print(is_palindrome_brute_force(" "))  # Expected output: True

# Time and Space Complexity Analysis:
#
# Optimal Two-Pointer Solution (is_palindrome):
#   - Time Complexity: O(n) → We traverse the string once to clean it and once to check palindrome.
#   - Space Complexity: O(1)
#
# Brute Force Solution (is_palindrome_brute_force):
#   - Time Complexity: O(n) → Cleaning the string and reversing it both take O(n).
#   - Space Complexity: O(n) → We store the cleaned string.
