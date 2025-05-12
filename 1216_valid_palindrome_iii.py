"""
🔷 LeetCode 1216: Valid Palindrome III

A **K-Palindrome** is a string that can become a palindrome after removing at most `k` characters.

🧠 Task:
Given a string `s` and an integer `k`, determine if `s` can be transformed into a palindrome by removing at most `k` characters.

---

Example 1:
Input: s = "abcdeca", k = 2
Output: True
Explanation: Remove 'b' and 'e' to get "acdca", which is a palindrome.

---

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.
- 1 <= k <= s.length

---

We solve this with:
1. Brute Force (slow, for understanding)
2. Dynamic Programming (optimal)

"""
from typing import List

def isValidPalindrome_bruteforce(s: str, k: int) -> bool:
    """
    Brute-force: try removing up to k characters and check if any result is palindrome.
    (Not efficient for larger strings, exponential time)
    
    Time Complexity: O(2^n)
    Space Complexity: O(n) (recursion stack)
    """
    def dfs(left, right, k):
        if k < 0:
            return False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return dfs(left+1, right, k-1) or dfs(left, right-1, k-1)
        return True
    return dfs(0, len(s)-1, k)


def isValidPalindrome_dp(s: str, k: int) -> bool:
    """
    Dynamic Programming: minimize number of deletions to make string a palindrome.
    
    - Define dp[i][j] = minimum deletions needed to make s[i..j] a palindrome.
    - dp[i][j] = dp[i+1][j-1] if s[i] == s[j]
    - Otherwise, dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1] <= k

def isValidPalindrome_recursive(s: str, k: int) -> bool:
    """
    Recursive approach (DFS) to check if at most k characters can be removed.

    Time Complexity: Exponential (O(2^n)) without memoization
    Space Complexity: O(n) (recursion stack)
    
    🔵 Important Notes:

    This is slow for large s because many states repeat.

    We can optimize it using memoization (dynamic programming)!

    ✅ With memoization (adding @lru_cache(None) or a DP table), it becomes O(n²)    

    """

    def dfs(left: int, right: int, k: int) -> bool:
        if k < 0:
            return False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return dfs(left+1, right, k-1) or dfs(left, right-1, k-1)
        return True

    return dfs(0, len(s) - 1, k)
    




# ------------- Sample tests -------------
if __name__ == "__main__":
    test_cases = [
        ("abcdeca", 2, True),
        ("abbababa", 1, True),
        ("abcdef", 1, False),
        ("a", 0, True),
        ("racecar", 0, True),
    ]
    for s, k, expected in test_cases:
        print(f"Input: s = {s}, k = {k}")
        print(f"Brute Force Output: {isValidPalindrome_bruteforce(s, k)}")
        print(f"DP Output         : {isValidPalindrome_dp(s, k)}")
        print(f"Expected          : {expected}")
        print("-----")



"""
✅ Complexity Summary:
- Brute-force:
    Time:  O(2^n)
    Space: O(n)

- Dynamic Programming:
    Time:  O(n²)
    Space: O(n²)
"""
