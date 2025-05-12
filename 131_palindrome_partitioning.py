"""
🔵 LeetCode 131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

-----------------------------------
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

-----------------------------------
Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters
"""

from typing import List

def partition(s: str) -> List[List[str]]:
    """
    ✅ Backtracking with Palindrome Checking

    Idea:
    - Use backtracking to try every possible prefix that forms a palindrome.
    - Recurse on the remaining substring.
    - Use a helper function to check if a string is a palindrome.

    Time Complexity: O(2^n) (exponential, as we consider all partitions)
    Space Complexity: O(n) for recursion stack (excluding result storage)
    """
    res = []

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def backtrack(start: int, path: List[str]):
        if start == len(s):
            res.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                path.append(prefix)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return res


# ✅ Sample Test Cases
if __name__ == "__main__":
    print(partition("aab"))  # [["a","a","b"],["aa","b"]]
    print(partition("a"))    # [["a"]]
    print(partition("aaba")) # [["a","a","b","a"],["a","aba"],["aa","b","a"]]
