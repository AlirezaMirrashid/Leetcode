"""
🔵 LeetCode 1. Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

Constraints:
- Each input has exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

-----------------------------------
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

-----------------------------------
Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    ✅ Optimal Solution (Hash Map)
    
    Idea:
    - Store each number in a hash map with its index.
    - For every number, check if (target - number) exists in the map.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []  # Should never reach here


def two_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    ❌ Brute Force Solution
    
    Idea:
    - Try every pair using nested loops.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ✅ Sample Test Cases
if __name__ == "__main__":
    nums1, target1 = [2, 7, 11, 15], 9
    print("Optimal:", two_sum(nums1, target1))  # [0, 1]
    
    nums2, target2 = [3, 2, 4], 6
    print("Optimal:", two_sum(nums2, target2))  # [1, 2]

    nums3, target3 = [3, 3], 6
    print("Optimal:", two_sum(nums3, target3))  # [0, 1]

    print("Brute Force:", two_sum_brute(nums1, target1))  # [0, 1]
    print("Brute Force:", two_sum_brute(nums2, target2))  # [1, 2]
    print("Brute Force:", two_sum_brute(nums3, target3))  # [0, 1]
