"""
🔷 LeetCode 76 - Minimum Window Substring

🧠 Task:
Given two strings `s` (length m) and `t` (length n), return the minimum window substring of `s`
such that every character in `t` (including duplicates) is included in the window.
If no such window exists, return the empty string "".
The answer is guaranteed to be unique.

-----------------------------------
Example 1:
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input:  s = "a", t = "a"
Output: "a"

Example 3:
Input:  s = "a", t = "aa"
Output: ""
Explanation: `t` has two 'a's but `s` only has one.

-----------------------------------
Constraints:
    - m == len(s), n == len(t)
    - 1 <= m, n <= 10^5
    - `s` and `t` consist of uppercase and lowercase English letters.

Follow-up:
    Can you implement an O(m + n) time algorithm?
"""

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        ✅ Optimal Sliding Window Approach
        
        Use two pointers (left, right) to form a window over `s`. Maintain a count of how many
        characters from `t` are currently satisfied. Expand `right` to include new chars, and
        contract `left` whenever all of `t` is covered to shorten the window.

        ⏱ Time Complexity: O(m + n)
        💾 Space Complexity: O(|Σ| + n) where Σ is the charset size
        
        Args:
            s (str): The source string.
            t (str): The target string of required characters.
        
        Returns:
            str: The minimum window in `s` containing all of `t`.
        """
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        # Expand `right` over s
        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # When all characters are covered, contract `left`
            while missing == 0:
                if end == 0 or right - left < end - start:
                    start, end = left, right
                # Try to move left up, releasing one char
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return s[start:end]

    def minWindowBruteForce(self, s: str, t: str) -> str:
        """
        ❌ Brute Force Approach
        
        Check every possible substring of `s` (start, end) of length >= len(t), test whether it contains
        all of `t`'s characters (via Counter containment). Track the shortest valid substring.

        ⏱ Time Complexity: O(m^2 * |Σ|) in worst case (m = len(s)).
        💾 Space Complexity: O(m + n)
        
        Args:
            s (str): The source string.
            t (str): The target string.
        
        Returns:
            str: The minimum window in `s` containing all of `t`.
        """
        if not s or not t or len(t) > len(s):
            return ""

        target_count = Counter(t)
        best = ""
        m = len(s)

        for i in range(m):
            for j in range(i + len(t), m + 1):
                window = s[i:j]
                if not best or j - i < len(best):
                    # Compare counts
                    if not (target_count - Counter(window)):
                        best = window
        return best


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aaflslflsldkalskaaa", "aaa", "aaa"),
    ]
    for s, t, expected in tests:
        print(f"s={s!r}, t={t!r}")
        print("Optimal   →", sol.minWindow(s, t))
        print("Brute     →", sol.minWindowBruteForce(s, t))
        print("Expected  →", expected)
        print("------------")

# ------------------------------------------------
# ✅ Optimal Sliding Window:
#     Time Complexity: O(m + n)
#     Space Complexity: O(|Σ| + n)
#
# ❌ Brute Force:
#     Time Complexity: O(m^2 * |Σ|)
#     Space Complexity: O(m + n)
