"""
🔷 LeetCode 647: Palindromic Substrings

🧠 Task:
Given a string `s`, return the number of palindromic substrings in it.
A substring is a contiguous sequence of characters in a string.
A palindrome is a string that reads the same backward as forward.

-----------------------------------
Example 1:
Input: s = "abc"
Output: 3
Explanation: The palindromic substrings are "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: The palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".

-----------------------------------
Constraints:
    - 1 <= s.length <= 1000
    - s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        ✅ Center Expansion Approach
        
        Approach:
          - Iterate through each character in s and treat each character as a potential center.
          - Expand outward from the center for both odd-length (single-center) palindromes 
            and even-length (two-center) palindromes.
          - Count each valid palindrome found during the expansions.
        
        ⏱ Time Complexity: O(n^2) in the worst case, where n is the length of s.
        💾 Space Complexity: O(1), as we use only a constant amount of extra space.
        
        Args:
            s (str): The input string.
        
        Returns:
            int: The total number of palindromic substrings in s.
        """
        total_count = 0
        for i in range(len(s)):
            total_count += self.expandAroundCenter(s, i, i)   # Odd-length palindromes
            total_count += self.expandAroundCenter(s, i, i+1)  # Even-length palindromes
        return total_count

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        """
        Expands outward from the indices left and right while the substring remains a palindrome.
        
        Args:
            s (str): The input string.
            left (int): The starting left index of the center.
            right (int): The starting right index of the center.
        
        Returns:
            int: The number of palindromic substrings found from this center expansion.
        """
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def countSubstringsBrute(self, s: str) -> int:
        """
        ❌ Brute Force Approach
        
        Idea:
          - Iterate over all possible substrings and check if they are palindromic.
          - Increment the count for each palindromic substring.
        
        ⏱ Time Complexity: O(n^3) in the worst case (n = len(s)).
        💾 Space Complexity: O(1) aside from the input and temporary substring.
        
        Args:
            s (str): The input string.
        
        Returns:
            int: The total number of palindromic substrings in s.
        """
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    count += 1
        return count

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        """
        Checks if the substring s[left:right+1] is a palindrome.
        
        Args:
            s (str): The input string.
            left (int): The left index of the substring.
            right (int): The right index of the substring.
        
        Returns:
            bool: True if the substring is a palindrome, False otherwise.
        """
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 🔸 Sample Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Example 1 Output:", sol.countSubstrings("abc"))   # Expected: 3
    print("Example 2 Output:", sol.countSubstrings("aaa"))   # Expected: 6

# ------------------------------------------------
# ✅ Time Complexity: O(n^2), where n is the length of the string.
# ✅ Space Complexity: O(1), as only a constant amount of extra space is used.

# ✅ Brute Force Approach:
#      Time Complexity: O(n^3)
#      Space Complexity: O(1)