"""
🔵 LeetCode 242: Valid Anagram

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.  
An **anagram** means both strings contain the exact same characters in any order.

-----------------------------------
Example 1:
Input: s = "anagram", t = "nagaram"  
Output: True  

Example 2:
Input: s = "rat", t = "car"  
Output: False  

Constraints:
- 1 ≤ s.length, t.length ≤ 5·10⁴  
- s and t consist of lowercase English letters.  

Follow-up: What if the inputs contain Unicode characters? How would you adapt?

---
"""

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Determine if t is an anagram of s.

    We count the frequency of each character in s and in t, and compare.
    
    Time Complexity: O(n) where n = len(s) + len(t)
    Space Complexity: O(k) where k = number of distinct characters (≤ 26 for lowercase)
    """
    # Quick length check
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)


# Follow-up: support full Unicode
def is_anagram_unicode(s: str, t: str) -> bool:
    """
    For Unicode, the same idea applies: count code‐points rather than assuming 'a'–'z'.

    Time Complexity: O(n)
    Space Complexity: O(u) where u = distinct Unicode code‐points in s/t
    """
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]
    return not freq


# --- Sample test runs ---
if __name__ == "__main__":
    tests = [
        ("anagram","nagaram", True),
        ("rat","car",      False),
        ("",   "",         True),
        ("a","á",          False),  # unicode example
    ]
    for s,t,exp in tests:
        res1 = is_anagram(s,t)
        res2 = is_anagram_unicode(s,t)
        print(f"{s!r}, {t!r} -> {res1} (ascii), {res2} (unicode), expected {exp}")
