"""
🔷 LeetCode 5: Longest Palindromic Substring

🧠 Task:
Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same backward as forward.

-----------------------------------
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

-----------------------------------
Constraints:
    - 1 <= s.length <= 1000
    - s consists of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        ✅ Optimal Approach using Center Expansion
        
        Approach:
          - For each index in the string, consider it as the center of a palindrome.
          - Expand around the center to cover both odd-length (single center) 
            and even-length (two centers) palindromes.
          - Track the longest palindrome found during these expansions.
        
        ⏱ Time Complexity: O(n^2) in the worst case.
        💾 Space Complexity: O(1)
        
        Args:
            s (str): The input string.
            
        Returns:
            str: The longest palindromic substring in s.
        """
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_pal = expandAroundCenter(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal
            
            # Even-length palindrome
            even_pal = expandAroundCenter(i, i + 1)
            if len(even_pal) > len(longest):
                longest = even_pal
        
        return longest

    def longestPalindromeBruteForce(self, s: str) -> str:
        """
        ❌ Brute Force Approach
        
        Approach:
          - Generate all possible substrings of s.
          - Check each substring to determine if it is a palindrome.
          - Track the longest palindrome found.
        
        ⏱ Time Complexity: O(n^3) in the worst case.
        💾 Space Complexity: O(1) aside from the space to store the longest palindrome.
        
        Args:
            s (str): The input string.
            
        Returns:
            str: The longest palindromic substring in s.
        """
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        n = len(s)
        longest = ""
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if isPalindrome(substring) and len(substring) > len(longest):
                    longest = substring
        return longest


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "babad",   # Expected: "bab" or "aba"
        "cbbd",    # Expected: "bb"
        "a",       # Expected: "a"
        "ac",      # Expected: "a" or "c"
        "forgeeksskeegfor",  # Expected: "geeksskeeg"
    ]
    
    for s in test_cases:
        print(f"Input: {s}")
        print("Center Expansion Output:", sol.longestPalindrome(s))
        print("Brute Force Output     :", sol.longestPalindromeBruteForce(s))
        print("------------")

# ------------------------------------------------
# ✅ Optimal Center Expansion:
#      Time Complexity: O(n^2)
#      Space Complexity: O(1)
#
# ✅ Brute Force Approach:
#      Time Complexity: O(n^3)
#      Space Complexity: O(1)
