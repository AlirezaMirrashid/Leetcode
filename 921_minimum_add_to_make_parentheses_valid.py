"""
🔷 LeetCode 921 - Minimum Add to Make Parentheses Valid

🧠 Task:
A parentheses string is valid if and only if:
  1. It is the empty string,
  2. It can be written as AB (A concatenated with B), where A and B are valid,
  3. It can be written as (A), where A is valid.

Given a parentheses string s, in one move you can insert a parenthesis at any position.
Return the minimum number of moves required to make s valid.

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3

Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        ✅ One-pass counter approach

        Maintain two counters:
          - balance: current net open parentheses ( '(' increments, ')' decrements )
          - additions: number of insertions needed so far

        If balance falls below 0, we need an extra '(' (additions += 1) and reset balance to 0.
        At end, any positive balance needs that many ')' insertions.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        balance = 0
        additions = 0
        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    additions += 1
                    balance = 0
        return additions + balance

    def minAddToMakeValidStack(self, s: str) -> int:
        """
        🧰 Stack-based approach

        Push '(' onto stack. For ')' if top is '(', pop; else count a required '(' insertion.
        At end, stack size is number of unmatched '(' needing ')'.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        insertions = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    insertions += 1
        # remaining '(' need ')'
        return insertions + len(stack)
