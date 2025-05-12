"""
🔷 LeetCode 8: String to Integer (atoi)

Implement the function `myAtoi(string s)` which converts a string to a 32-bit signed integer (similar to C/C++’s atoi).

The algorithm for `myAtoi(s)` is:
1. Discard as many whitespace characters as necessary until the first non-whitespace character is found.
2. Then, if the next character is '-' or '+', read it in to determine the sign of the final number. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer. If no digits were read, the integer is 0. Apply the sign as determined in step 2.
5. If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 − 1]`, clamp the integer so that it remains in the range. Specifically,
   - values less than −2^31 should be clamped to −2^31,
   - values greater than 2^31 − 1 should be clamped to 2^31 − 1.
6. Return the integer as the final result.

Example 1:
    Input: s = "42"
    Output: 42
    Explanation: Reads "42", returns 42.

Example 2:
    Input: s = "   -042"
    Output: -42
    Explanation: Leading spaces ignored, '-' sign read, "042" → 42, apply sign → -42.

Example 3:
    Input: s = "1337c0d3"
    Output: 1337
    Explanation: Reads "1337", stops at 'c'.

Example 4:
    Input: s = "0-1"
    Output: 0
    Explanation: Reads "0", stops at '-', returns 0.

Example 5:
    Input: s = "words and 987"
    Output: 0
    Explanation: First non-whitespace is 'w', not digit or sign → 0.

Constraints:
    0 <= s.length <= 200
    s consists of English letters, digits, ' ', '+', '-', and '.'.
"""

def myAtoi(s: str) -> int:
    """
    Parse the string to a 32-bit signed integer according to the rules above.
    
    Time Complexity: O(n), where n = len(s), we scan the string at most once.
    Space Complexity: O(1), only a few integer variables are used.
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    i, n = 0, len(s)
    # 1) skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # 2) optional sign
    sign = 1
    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # 3) read digits
    result = 0
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')
        # 4) check for overflow/underflow before adding digit
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1

    return sign * result


if __name__ == "__main__":
    # Sample test cases
    tests = [
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("-91283472332", -2**31),  # underflow
        ("91283472332", 2**31 - 1), # overflow
        ("   +0 123", 0),
        ("", 0),
        ("   ", 0),
        ("+1", 1),
        ("-5-", -5),
    ]

    for s, expected in tests:
        output = myAtoi(s)
        print(f"Input: {s!r:15} → Output: {output:12}  Expected: {expected}")

"""
✅ Complexity:
- Time:  O(n)
- Space: O(1)
"""
