"""
🔵 LeetCode 392: Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string formed from the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the remaining characters (e.g., "ace" is a subsequence of "abcde" 
while "aec" is not).

-----------------------------------
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

-----------------------------------
Constraints:
    - 0 <= s.length <= 100
    - 0 <= t.length <= 10^4
    - s and t consist only of lowercase English letters.

Follow up:
    Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to see if 
    t has its subsequence. In this scenario, you could preprocess t by mapping each character to all its indices and then 
    use binary search for each query.
"""

from typing import List
import bisect

def is_subsequence(s: str, t: str) -> bool:
    """
    Optimal Two-Pointer Approach

    Approach:
      - Use two pointers: one for s and one for t.
      - Traverse t, and if the current character in t matches the current character in s, increment the s pointer.
      - If the s pointer reaches the end of s, then s is a subsequence of t.
    
    Time Complexity: O(n + m), where n = len(s) and m = len(t).
    Space Complexity: O(1)
    
    Args:
        s (str): The subsequence candidate.
        t (str): The target string.
    
    Returns:
        bool: True if s is a subsequence of t, False otherwise.
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def is_subsequence_followup(s: str, t: str) -> bool:
    """
    Follow-Up: Preprocessing with Binary Search Approach

    Approach:
      - Preprocess t by building a dictionary that maps each character to a list of its indices in t.
      - For each character in s, use binary search (via bisect) on the corresponding list in the dictionary 
        to find an index greater than the previous index found.
      - If for any character no valid index is found, return False.
    
    Time Complexity:
      - Preprocessing: O(m), where m = len(t)
      - Each query: O(n log m), where n = len(s)
    Space Complexity: O(m)
    
    Args:
        s (str): The subsequence candidate.
        t (str): The target string.
    
    Returns:
        bool: True if s is a subsequence of t, False otherwise.
    """
    # Preprocess t: Map each character to all its indices in t
    char_indices = {}
    for idx, char in enumerate(t):
        if char not in char_indices:
            char_indices[char] = []
        char_indices[char].append(idx)
    
    current_index = -1
    for char in s:
        if char not in char_indices:
            return False  # char not in t at all
        # Use bisect to find the first occurrence of char with index > current_index
        pos = bisect.bisect_right(char_indices[char], current_index)
        if pos == len(char_indices[char]):
            return False  # No valid index found
        current_index = char_indices[char][pos]
    
    return True

# Sample Test Cases
if __name__ == "__main__":
    # Testing the Two-Pointer Approach
    print("Two-Pointer Approach:")
    print(is_subsequence("abc", "ahbgdc"))  # Expected: True
    print(is_subsequence("axc", "ahbgdc"))  # Expected: False

    # Testing the Follow-Up Binary Search Approach:
    print("\nFollow-Up (Preprocessing & Binary Search) Approach:")
    print(is_subsequence_followup("abc", "ahbgdc"))  # Expected: True
    print(is_subsequence_followup("axc", "ahbgdc"))  # Expected: False

# ------------------------------------------------
# ✅ Time Complexity:
#      - Two-Pointer Approach: O(n + m), where n = len(s) and m = len(t)
#      - Follow-Up Approach: Preprocessing O(m) and each query O(n log m)
# ✅ Space Complexity:
#      - Two-Pointer Approach: O(1)
#      - Follow-Up Approach: O(m), where m is the length of t
