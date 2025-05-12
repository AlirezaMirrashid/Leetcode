"""
🔵 LeetCode 93. Restore IP Addresses

A valid IP address consists of exactly four integers (0 to 255) separated by dots. Each integer cannot have leading zeros.

Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`.

-----------------------------------
Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

-----------------------------------
Constraints:
- 1 <= s.length <= 20
- s consists of digits only.
"""

from typing import List

def restore_ip_addresses(s: str) -> List[str]:
    """
    ✅ Backtracking Approach

    Idea:
    - An IP address has exactly 4 parts.
    - Use backtracking to explore each split of 1 to 3 digits.
    - Skip invalid segments (e.g., > 255 or leading zeros).

    Time Complexity: O(1) → because max valid IPs are bounded (~27 in worst case)
    Space Complexity: O(1) → excluding result storage
    """
    def is_valid(segment: str) -> bool:
        # Must not be empty, <= 255, and no leading zeros unless it's '0'
        return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

    def backtrack(start: int, parts: List[str]):
        if len(parts) == 4:
            if start == len(s):
                result.append('.'.join(parts))
            return

        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]
            if is_valid(segment):
                backtrack(start + length, parts + [segment])

    result = []
    backtrack(0, [])
    return result


# ✅ Sample Test Cases
if __name__ == "__main__":
    s1 = "25525511135"
    print("Output:", restore_ip_addresses(s1))  # ["255.255.11.135", "255.255.111.35"]

    s2 = "0000"
    print("Output:", restore_ip_addresses(s2))  # ["0.0.0.0"]

    s3 = "101023"
    print("Output:", restore_ip_addresses(s3))
    # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
