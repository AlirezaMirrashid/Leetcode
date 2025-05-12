"""
🔵 LeetCode 72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You can perform the following operations:
- Insert a character
- Delete a character
- Replace a character

-----------------------------------
Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (delete 'r')
rose -> ros (delete 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (delete 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

-----------------------------------
Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters
"""

def minDistance(word1: str, word2: str) -> int:
    """
    ✅ Dynamic Programming

    Idea:
    - Use a 2D DP table where dp[i][j] represents the minimum edit distance
      to convert word1[0:i] to word2[0:j].
    - If characters match, no operation needed.
    - Otherwise, take the min of insert, delete, or replace.

    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: converting to/from empty string
    for i in range(m + 1):
        dp[i][0] = i  # delete all
    for j in range(n + 1):
        dp[0][j] = j  # insert all

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i][j - 1]
                delete = dp[i - 1][j]
                replace = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(insert, delete, replace)

    return dp[m][n]


# ✅ Sample Test Cases
if __name__ == "__main__":
    print(minDistance("horse", "ros"))         # Output: 3
    print(minDistance("intention", "execution")) # Output: 5
    print(minDistance("", "abc"))              # Output: 3
    print(minDistance("abc", ""))              # Output: 3
    print(minDistance("abc", "abc"))           # Output: 0
