"""
🔵 LeetCode 


Given an array `nums` of distinct integers, return all possible permutations of the array.
You may return the answer in any order.

-----------------------------------
Example 1:
Input: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Example 2:
Input: nums = [0, 1]
Output: [[0,1], [1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

-----------------------------------
Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All elements of nums are unique.
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    """
    ✅ Backtracking Approach

    Idea:
    - Use DFS to build permutations by choosing each element one by one.
    - Track used elements to avoid duplicates.

    Time Complexity: O(n!)
    Space Complexity: O(n) recursion stack + result storage
    """
    def backtrack(path: List[int], used: List[bool]):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False

    result = []
    backtrack([], [False] * len(nums))
    return result


def permute_builtin(nums: List[int]) -> List[List[int]]:
    """
    ✅ Alternative: Using itertools.permutations

    Time Complexity: O(n!)
    Space Complexity: O(n!)
    """
    from itertools import permutations
    return list(permutations(nums))


# ✅ Sample Test Cases
if __name__ == "__main__":
    nums1 = [1, 2, 3]
    print("Backtracking:", permute(nums1))  # [[1,2,3], [1,3,2], ...]

    nums2 = [0, 1]
    print("Backtracking:", permute(nums2))  # [[0,1], [1,0]]

    nums3 = [1]
    print("Backtracking:", permute(nums3))  # [[1]]

    print("Built-in:", permute_builtin(nums1))  # Same results, different method
