"""
LeetCode 1768: Merge Strings Alternately
Problem Link: https://leetcode.com/problems/merge-strings-alternately/

Description:
    You are given two strings word1 and word2. Merge the strings by adding letters in 
    alternating order, starting with word1. If a string is longer than the other, append 
    the additional letters onto the end of the merged string.

Examples:
    Example 1:
        Input: word1 = "abc", word2 = "pqr"
        Output: "apbqcr"
        Explanation:
            word1:  a   b   c
            word2:    p   q   r
            merged: a p b q c r

    Example 2:
        Input: word1 = "ab", word2 = "pqrs"
        Output: "apbqrs"
        Explanation:
            word1:  a   b 
            word2:    p   q   r   s
            merged: a p b q   r   s

    Example 3:
        Input: word1 = "abcd", word2 = "pq"
        Output: "apbqcd"
        Explanation:
            word1:  a   b   c   d
            word2:    p   q 
            merged: a p b q c   d

Constraints:
    - 1 <= word1.length, word2.length <= 100
    - word1 and word2 consist of lowercase English letters.
"""

def merge_alternately(word1: str, word2: str) -> str:
    """
    Merges two strings alternately, starting with word1. If one string is longer,
    appends the additional letters at the end of the merged string.

    Parameters:
        word1 (str): The first input string.
        word2 (str): The second input string.

    Returns:
        str: The merged string.

    Time Complexity:
        O(n + m) where n = len(word1) and m = len(word2) since we iterate through both strings once.
    
    Space Complexity:
        O(n + m) for the result string.
    """
    i, j = 0, 0
    merged = []

    # Merge letters in alternating order while both strings have remaining characters.
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    # Append any remaining characters from word1 or word2.
    if i < len(word1):
        merged.append(word1[i:])
    if j < len(word2):
        merged.append(word2[j:])

    return "".join(merged)


# Example test cases:
if __name__ == "__main__":
    # Example 1:
    word1_ex1 = "abc"
    word2_ex1 = "pqr"
    print("Example 1 Output:", merge_alternately(word1_ex1, word2_ex1))  # Expected: "apbqcr"

    # Example 2:
    word1_ex2 = "ab"
    word2_ex2 = "pqrs"
    print("Example 2 Output:", merge_alternately(word1_ex2, word2_ex2))  # Expected: "apbqrs"

    # Example 3:
    word1_ex3 = "abcd"
    word2_ex3 = "pq"
    print("Example 3 Output:", merge_alternately(word1_ex3, word2_ex3))  # Expected: "apbqcd"
