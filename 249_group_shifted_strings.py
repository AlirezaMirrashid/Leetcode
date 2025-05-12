"""
🔷 LeetCode 249 - Group Shifted Strings

🧠 Task:
Given a list of strings that consists only of lowercase letters, group all strings that belong to the same shifting sequence.

A shifting sequence is defined as follows: if we shift each letter of a string to its successive letter (with 'z' wrapping around to 'a'),
we obtain another string in the same sequence. For example, "abc" -> "bcd" -> ... -> "xyz". All strings with the same pattern of differences
between adjacent characters belong to the same group.

-----------------------------------
Example:
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Explanation:
- "abc", "bcd", and "xyz" all share the same pattern [1, 1] (shifting differences modulo 26).
- "az" and "ba" share the pattern [25] (or [-1] mod 26).
- "acef" has a unique pattern.
- Single-character strings are grouped together.
  
-----------------------------------
Constraints:
    - 1 <= strings.length <= 10^4
    - 1 <= strings[i].length <= 100
    - strings[i] consists only of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Groups shifted strings based on their difference signature.
        
        Approach:
          - For each string, compute a signature based on the differences between consecutive characters
            modulo 26. This signature is represented as a tuple.
          - Strings of length 1 have an empty signature and are grouped together.
          - Use a dictionary to aggregate strings with the same signature.
        
        ⏱ Time Complexity: O(m * n), where m is the number of strings and n is the average length of each string.
        💾 Space Complexity: O(m * n) in the worst-case, for storing the signatures and resulting groups.
        
        Args:
            strings (List[str]): The list of strings to group.
        
        Returns:
            List[List[str]]: A list of grouped shifted strings.
        """
        groups = defaultdict(list)
        for s in strings:
            # For single-letter strings, use an empty tuple as the signature
            if len(s) < 2:
                key = () # or (-1, )
            else:
                key = tuple((ord(s[i]) - ord(s[i-1])) % 26 for i in range(1, len(s)))
            groups[key].append(s)
        
        return list(groups.values())
    
    def groupStringsBruteForce(self, strings: List[str]) -> List[List[str]]:
        """
        ❌ Brute Force Approach (Comparison-based)
        
        Approach:
          - Compare every pair of strings to determine if they belong in the same shifting group.
          - This approach is less efficient and is provided for comparison.
        
        ⏱ Time Complexity: O(m^2 * n), where m is the number of strings and n is the average string length.
        💾 Space Complexity: O(m * n) for storing groups.
        
        Args:
            strings (List[str]): The list of strings to group.
        
        Returns:
            List[List[str]]: A list of grouped shifted strings.
        """
        def sameGroup(s1: str, s2: str) -> bool:
            # Two strings are in the same shifted group if they have the same length and their
            # differences between consecutive letters (mod 26) are equal.
            if len(s1) != len(s2):
                return False
            if len(s1) < 2:
                return True  # all single-letter strings are in the same group
            diff1 = [(ord(s1[i]) - ord(s1[i-1])) % 26 for i in range(1, len(s1))]
            diff2 = [(ord(s2[i]) - ord(s2[i-1])) % 26 for i in range(1, len(s2))]
            return diff1 == diff2
        
        groups = []
        for s in strings:
            found = False
            for group in groups:
                # Compare with the first string of the group for group signature
                if sameGroup(s, group[0]):
                    group.append(s)
                    found = True
                    break
            if not found:
                groups.append([s])
                
        return groups


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    test_strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print("Optimal Approach Output:")
    for group in sol.groupStrings(test_strings):
        print(group)
    
    print("\nBrute Force Approach Output:")
    for group in sol.groupStringsBruteForce(test_strings):
        print(group)

# ------------------------------------------------
# ✅ Optimal Approach:
#      Time Complexity: O(m * n) 
#      Space Complexity: O(m * n)
#
# ✅ Brute Force Approach:
#      Time Complexity: O(m^2 * n)
#      Space Complexity: O(m * n)
