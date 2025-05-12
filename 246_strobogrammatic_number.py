"""
🔷 LeetCode 246: Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees 
(i.e., looked at upside down).  Each digit must map to a valid digit when rotated:
  - '0' ↔ '0'
  - '1' ↔ '1'
  - '6' ↔ '9'
  - '8' ↔ '8'
  - '9' ↔ '6'

Write a function to determine if a number (given as a string) is strobogrammatic.

Example 1:
    Input: "69"
    Output: True
    Explanation: '6' becomes '9', '9' becomes '6' → "69" reversed is "96", matches original.

Example 2:
    Input: "88"
    Output: True
    Explanation: '8'→'8', '8'→'8' → reversed mapped string is "88".

Example 3:
    Input: "962"
    Output: False
    Explanation: '2' has no valid mapping.

Constraints:
    1 ≤ s.length ≤ 50
    s consists only of digits.

We provide two methods:
 1. Two-pointer in-place check (O(n) time, O(1) extra space)
 2. Build & compare mapped string (O(n) time, O(n) space)
"""

from typing import Dict

# Method 1: Two-pointer check, constant extra space
def isStrobogrammatic_two_pointer(num: str) -> bool:
    """
    Use two pointers (i, j) from the ends toward center.
    At each step, check that num[i] maps to num[j] under the strobogrammatic mapping.
    
    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    mapping: Dict[str, str] = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    i, j = 0, len(num) - 1
    while i <= j:
        c1, c2 = num[i], num[j]
        # if c1 not mappable or its mapping ≠ c2, fail
        if c1 not in mapping or mapping[c1] != c2:
            return False
        i += 1
        j -= 1
    return True

# Method 2: Build rotated string and compare
def isStrobogrammatic_build_map(num: str) -> bool:
    """
    Build the rotated version: map each digit, then reverse the mapped string.
    Compare with original.
    
    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    mapping: Dict[str, str] = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    # attempt to map every character
    mapped = []
    for ch in num:
        if ch not in mapping:
            return False
        mapped.append(mapping[ch])
    # reverse the mapped list and join
    rotated = "".join(reversed(mapped))
    return rotated == num

# ------------- Sample tests -------------
if __name__ == "__main__":
    test_cases = [
        ("69", True),
        ("88", True),
        ("962", False),
        ("818", True),
        ("619", True),  # "619" → map→["9","1","6"] → reverse→"619"
        ("2", False),
        ("", True),     # empty string considered strobogrammatic by vacuous truth
        ("10", False),  # "10" → map→["1","0"] → reverse→"01" ≠ "10"
    ]
    for s, expected in test_cases:
        out1 = isStrobogrammatic_two_pointer(s)
        out2 = isStrobogrammatic_build_map(s)
        print(f"Input: {s!r:5} → two_pointer: {out1}, build_map: {out2}, expected: {expected}")

"""
✅ Complexity Summary:

Method 1 (two_pointer):
    Time:  O(n)
    Space: O(1)

Method 2 (build_map):
    Time:  O(n)
    Space: O(n)
"""
