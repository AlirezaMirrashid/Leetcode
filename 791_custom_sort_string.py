"""
LeetCode 791: Custom Sort String
Problem Link: https://leetcode.com/problems/custom-sort-string/

Description:
    You are given two strings order and s. All the characters of order are unique and were sorted 
    in some custom order previously.

    Permute the characters of s so that they match the order that order was sorted. More specifically, 
    if a character x occurs before a character y in order, then x should occur before y in the permuted string.

    Return any permutation of s that satisfies this property.

Examples:
    Example 1:
        Input: order = "cba", s = "abcd"
        Output: "cbad"
        Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
                     Since "d" does not appear in order, it can be at any position.
                     
    Example 2:
        Input: order = "bcafg", s = "abcd"
        Output: "bcad"
        Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. 
                     The character "d" in s does not appear in order, so its position is flexible.

Constraints:
    - 1 <= order.length <= 26
    - 1 <= s.length <= 200
    - order and s consist of lowercase English letters.
    - All the characters of order are unique.
"""

from typing import Dict

# Optimal Counting Approach
def custom_sort_string(order: str, s: str) -> str:
    """
    Returns a permutation of s such that characters appear in the order defined by order.
    
    This approach counts the frequency of each character in s, then constructs the result:
      1. For every character in order, add that character (count times) to the result.
      2. Append the remaining characters (those not in order) in any order (preserving their occurrence in s).

    Parameters:
        order (str): A string representing the custom order.
        s (str): The string to be sorted.
    
    Returns:
        str: A permutation of s following the custom order.
    """
    # Count frequency of characters in s
    freq: Dict[str, int] = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    result = []
    
    # Append characters in the order given by 'order'
    for ch in order:
        if ch in freq:
            result.append(ch * freq[ch])
            del freq[ch]  # Remove processed characters
    
    # Append remaining characters (those not in 'order')
    for ch, count in freq.items():
        result.append(ch * count)
    
    return "".join(result)


# Sorting Approach Using Custom Key
def custom_sort_string_sorting(order: str, s: str) -> str:
    """
    Returns a permutation of s sorted by a custom key based on order.
    
    Characters found in 'order' are given a priority based on their index in 'order'. 
    Characters not in 'order' are given a default large index so they appear at the end.
    
    Parameters:
        order (str): A string representing the custom order.
        s (str): The string to be sorted.
    
    Returns:
        str: A permutation of s following the custom order.
    """
    order_index = {ch: i for i, ch in enumerate(order)}
    # Use order_index.get(ch, len(order)) so that characters not in 'order' have lower priority
    sorted_chars = sorted(s, key=lambda ch: order_index.get(ch, len(order)))
    return "".join(sorted_chars)


# Example test cases:
if __name__ == "__main__":
    # Example 1
    order1 = "cba"
    s1 = "abcd"
    print("Optimal Counting Approach:", custom_sort_string(order1, s1))  # Expected output: "cbad" (or any valid permutation)
    print("Sorting Approach:", custom_sort_string_sorting(order1, s1))   # Expected output: "cbad" or similar
    
    # Example 2
    order2 = "bcafg"
    s2 = "abcd"
    print("Optimal Counting Approach:", custom_sort_string(order2, s2))  # Expected output: "bcad"
    print("Sorting Approach:", custom_sort_string_sorting(order2, s2))   # Expected output: "bcad" or similar

# Time and Space Complexity Analysis:
#
# Optimal Counting Approach (custom_sort_string):
#   - Time Complexity: O(n + m) where n = len(s) and m = len(order), since we count frequencies and then build the result.
#   - Space Complexity: O(n) for the frequency dictionary and result storage.
#
# Sorting Approach (custom_sort_string_sorting):
#   - Time Complexity: O(n log n) due to sorting.
#   - Space Complexity: O(n) for sorting storage.
