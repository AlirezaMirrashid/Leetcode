"""
🔵 LeetCode 14: Longest Common Prefix

You are given an array of strings. Write a function to find the longest common prefix string amongst the strings.

If there is no common prefix, return an empty string "".

-----------------------------------
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Explanation: The longest common prefix among these strings is "fl".

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

-----------------------------------

Constraints:
    - 1 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    This function finds the longest common prefix among a list of strings.
    
    Approach:
      - Iterate through each character index of the first string and check if all the strings
        share the same character at the current index.
      - If any string is shorter than the current index or has a different character, we stop and
        return the prefix found so far.
    

    Parameters:
        strs (List[str]): A list of strings for which we need to find the longest common prefix.
    
    Returns:
        str: The longest common prefix string.
    """
    if not strs:
        return ""
    
    res = ""
    for i in range(len(strs[0])):  # Loop through each character of the first string
        for s in strs:  # Check this character in all other strings
            # If the current string is shorter than the index or does not match the current character, return the result
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]  # Add the character to the result if all strings match
    
    return res

# Sample Test Cases
if __name__ == "__main__":
    strs_1 = ["flower", "flow", "flight"]
    print("Example 1 Output:", longestCommonPrefix(strs_1))  # Expected: "fl"

    strs_2 = ["dog", "racecar", "car"]
    print("Example 2 Output:", longestCommonPrefix(strs_2))  # Expected: ""

# ------------------------------------------------
# ✅ Time Complexity: O(S), where S is the sum of the lengths of all strings in the input list strs.
# ✅ Space Complexity: O(1), as we are only modifying a single prefix string.
