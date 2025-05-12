"""
🔷 LeetCode 49: Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
    Explanation:
      - "eat", "tea", "ate" are anagrams of each other.
      - "tan", "nat" are anagrams of each other.
      - "bat" has no anagram in the list.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10⁴
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

We present three approaches:
 1. Brute-force grouping         – O(n² · k log k) time  
 2. Sort-characters as key        – O(n · k log k) time  
 3. Count-frequency tuple as key  – O(n · k) time  
where n = number of strings, k = max length of a string.
"""

from collections import defaultdict
from typing import List, Tuple

def groupAnagrams_bruteforce(strs: List[str]) -> List[List[str]]:
    """
    Brute-force: for each string, compare (by sorting) to a representative of each existing group.
    If matches, add to that group; otherwise start a new group.
    
    Time Complexity: O(n² · k log k)
      - For each of n strings, in worst case compare to O(n) groups,
        each comparison costs O(k log k) to sort the string.
    Space Complexity: O(n · k) to store the output groups.
    """
    groups: List[List[str]] = []
    reps: List[str] = []  # representative string for each group

    for s in strs:
        placed = False
        for gi, rep in enumerate(reps):
            if sorted(s) == sorted(rep):
                groups[gi].append(s)
                placed = True
                break
        if not placed:
            reps.append(s)
            groups.append([s])
    return groups

def groupAnagrams_sort(strs: List[str]) -> List[List[str]]:
    """
    Use sorted string as the hash key.
    
    Time Complexity: O(n · k log k)
      - Sorting each string of length k costs O(k log k), done n times.
    Space Complexity: O(n · k) for keys and output.
    """
    d: defaultdict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        d[key].append(s)
    return list(d.values())

def groupAnagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Use character frequency count (26-length tuple) as the hash key.
    
    Time Complexity: O(n · k)
      - Counting k characters per string, building a tuple of length 26.
    Space Complexity: O(n · k) for keys and output.
    """
    d: defaultdict[Tuple[int,...], List[str]] = defaultdict(list)
    for s in strs:
        # count frequency of each lowercase letter
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        key = tuple(freq)
        d[key].append(s)
    return list(d.values())

# ------------- Sample tests -------------
if __name__ == "__main__":
    test_cases = [
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc","bca","cab","xyz","zyx","a"], [["abc","bca","cab"],["xyz","zyx"],["a"]]),
    ]
    for strs, expected in test_cases:
        out1 = groupAnagrams_bruteforce(strs)
        out2 = groupAnagrams_sort(strs)
        out3 = groupAnagrams_count(strs)
        print("Input:", strs)
        print(" Brute    ->", out1)
        print(" SortKey  ->", out2)
        print(" CountKey ->", out3)
        print(" Expected approx. groups (order may vary):", expected)
        print("---")

# ✅ Complexity Summary:
# 1. Brute-force:
#    Time:  O(n² · k log k)
#    Space: O(n · k)
#
# 2. Sort-characters key:
#    Time:  O(n · k log k)
#    Space: O(n · k)
#
# 3. Count-frequency key:
#    Time:  O(n · k)
#    Space: O(n · k)
