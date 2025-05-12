"""
🔷 LeetCode 65 - Valid Number

🧠 Task:
Given a string `s`, return whether `s` is a valid number. A valid number can be:
  - An integer with optional sign and optional exponent.
  - A decimal with optional sign and optional exponent.

Definitions:
  • Integer: [ '+' | '-' ] digits  
  • Decimal: [ '+' | '-' ] ( digits '.' [digits] | '.' digits )  
  • Exponent: [ 'e' | 'E' ] [ '+' | '-' ] digits  
  • A number may have **both** a decimal part and an exponent part.

-----------------------------------
Example 1:
Input:  s = "0"     → Output: True

Example 2:
Input:  s = "e"     → Output: False

Example 3:
Input:  s = "."     → Output: False

-----------------------------------
Constraints:
  - 1 <= s.length <= 20
  - `s` consists of only English letters, digits, '+', '-', or '.'.
"""

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        ✅ State-Machine / Flag-Based Parsing (O(n) time, O(1) space)

        We scan character by character, maintaining flags:
          - seen_digit:   we've seen at least one digit before any 'e'
          - seen_dot:     we've seen a decimal point
          - seen_exp:     we've seen an exponent 'e' or 'E'
          - digit_after:  after an exponent, we've seen at least one digit

        Rules:
          - A sign '+'/'-' is valid only at the start or immediately after 'e'/'E'.
          - A '.' is valid only if we haven't seen a dot or exponent yet.
          - An 'e'/'E' is valid only if we haven't seen one yet and we've seen a digit.
          - Anything else invalidates the string.

        Returns True only if we've seen at least one digit before any exponent
        and at least one digit after any exponent.
        """
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
                if seen_exp:
                    digit_after_exp = True
            elif ch in ['+', '-']:
                # valid only at start or right after an exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                # valid only if no dot yet and no exponent yet
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in ['e', 'E']:
                # valid only if no exp yet and we've seen a digit
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                digit_after_exp = False  # we now require at least one digit
            else:
                return False

        return seen_digit and digit_after_exp


    def isNumberRegex(self, s: str) -> bool:
        """
        ❌ Regex-Based Approach (O(1) extra space, O(n) to match)

        Use a single full-match regex that encodes the grammar:
          ^[+-]?     optional sign
           (         one of:
             \d+(\.\d*)?  digits with optional fractional part
            | \.\d+       or leading dot + digits
           )
           ([eE][+-]?\d+)?  optional exponent
          $
        """
        pattern = re.compile(r"""
            ^[+\-]?                    # optional sign
            (?:                        
               \d+(?:\.\d*)?           # digits, optional decimal
              | \.\d+                  # or leading dot + digits
            )
            (?:[eE][+\-]?\d+)?         # optional exponent
            $""", re.VERBOSE)
        return bool(pattern.match(s))


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("0", True), (" 0.1 ", True), ("abc", False),
        ("1 a", False), ("2e10", True), (" -90E3   ", True),
        (" 1e", False), ("e3", False), ("6e-1", True),
        ("99e2.5", False), ("--6", False), ("-+3", False),
        ("95a54e53", False), (".1", True), ("3.", True),
        (".", False), (" .e1", False)
    ]
    for s, ans in tests:
        print(f"{s!r:10} → {sol.isNumber(s):5}  (regex: {sol.isNumberRegex(s):5})  expected {ans}")

# ------------------------------------------------
# ✅ State-Machine Approach:
#     Time Complexity: O(n)
#     Space Complexity: O(1)
#
# ❌ Regex Approach:
#     Time Complexity: O(n)
#     Space Complexity: O(1)
