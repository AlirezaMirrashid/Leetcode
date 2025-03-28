# LeetCode 680: Valid Palindrome II
# Problem Link: https://leetcode.com/problems/valid-palindrome-ii/
#
# Description:
# Given a string s, return true if s can be a palindrome after deleting at most one character.
#
# Example 1:
# Input: s = "aba"
# Output: true
#
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
# Example 3:
# Input: s = "abc"
# Output: false
#
# Constraints:
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        """
        Determines if a string s can become a palindrome by deleting at most one character.
        Uses a two-pointer approach to check for mismatches and then verifies if one deletion fixes it.
        """
        l, r = 0, len(s) - 1

        # Use two pointers moving towards the center.
        while l < r:
            if s[l] != s[r]:
                # On a mismatch, try skipping the left character or the right character.
                # Slicing is used here to create substrings for checking.
                skip_left = s[l + 1:r + 1]
                skip_right = s[l:r]
                # Check if either resulting substring is a palindrome.
                # return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
                return self.is_palindrome(skip_left) or self.is_palindrome(skip_right)

            l += 1
            r -= 1

        # If no mismatches are found, the string is already a palindrome.
        return True
    def is_palindrome(self, subs: str) -> bool:
        l, r = 0, len(subs)
        while l < r:
            if subs[l] != subs[r]:
                return False
            l += 1
            r -= 1
        return True

# Brute Force Alternative Solution:
def valid_palindrome_brute_force(s: str) -> bool:
    """
    Brute-force approach: For each index, remove the character at that index and check if the resulting string is a palindrome.
    This approach has a higher time complexity.
    """

    def is_palindrome(subs: str) -> bool:
        return subs == subs[::-1]

    # If s is already a palindrome, return True.
    if is_palindrome(s):
        return True

    # Try deleting each character one by one.
    for i in range(len(s)):
        # Form a new string by skipping the character at index i.
        candidate = s[:i] + s[i + 1:]
        if is_palindrome(candidate):
            return True

    return False

solution_check = Solution()
# Example test cases:
print(solution_check.valid_palindrome("aba"))  # Expected output: True
print(solution_check.valid_palindrome("abca"))  # Expected output: True
print(solution_check.valid_palindrome("abc"))  # Expected output: False

# Testing the brute-force solution as well:
print(valid_palindrome_brute_force("aba"))  # Expected output: True
print(valid_palindrome_brute_force("abca"))  # Expected output: True
print(valid_palindrome_brute_force("abc"))  # Expected output: False

# Time and Space Complexity Analysis:
#
# Optimal Two-Pointer Solution (valid_palindrome):
#   Time Complexity: O(n)
#     - In the worst case, we traverse the string once using two pointers.
#     - In the event of a mismatch, we perform two substring reversals, each taking O(n) time.
#     - Overall, this results in O(n) time complexity.
#
#   Space Complexity: O(1)
#     - two pointer solution requires O(1) space.
#
# Brute-Force Solution (valid_palindrome_brute_force):
#   Time Complexity: O(n^2)
#     - For each of the n characters, we create a new substring (O(n)) and check if it's a palindrome (O(n)).
#     - This results in a worst-case time complexity of O(n^2).
#
#   Space Complexity: O(n)
#     - Slicing for each candidate string takes O(n) space.
