# LeetCode 560: Subarray Sum Equals k
# Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/
#
# Description:
# Given an integer array nums and an integer k, return the total number of subarrays
# whose sum equals k.
#
# Note:
# A subarray is a contiguous non-empty sequence of elements within an array.
#
# Example 1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
#
# Example 2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10^3 <= nums[i] <= 10^3
# -10^7 <= k <= 10^7

from typing import List
import collections


def subarray_sum(nums: List[int], k: int) -> int:
    """
    Optimal approach to find the number of subarrays with sum equal to k.

    Uses a prefix sum dictionary to store the frequency of each cumulative sum.
    For each element, the difference (current sum - k) indicates how many times a valid
    prefix has occurred that would form a subarray summing to k.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The target subarray sum.

    Returns:
        int: The total number of subarrays whose sum equals k.
    """
    res = 0  # To store the count of valid subarrays.
    cur_sum = 0  # To store the current cumulative sum.
    prefix_sums = {0: 1}  # Dictionary mapping cumulative sum to its frequency.
    # Start with 0:1 since a subarray starting at index 0 can have sum k.

    for num in nums:
        cur_sum += num  # Update the running cumulative sum.
        diff = cur_sum - k  # Calculate the required prefix sum for a valid subarray.
        res += prefix_sums.get(diff, 0)  # If diff exists, add its frequency to the result.
        # Update the dictionary with the current cumulative sum.
        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1

    return res


# Brute Force Alternative (Not Recommended for Large Inputs):
def subarray_sum_brute_force(nums: List[int], k: int) -> int:
    """
    Brute-force approach to find the number of subarrays with sum equal to k.

    For each possible subarray, calculate its sum and check if it equals k.
    This approach is less efficient with O(n^2) subarrays to check.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The target subarray sum.

    Returns:
        int: The total number of subarrays whose sum equals k.
    """
    count = 0
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1
    return count


# Example test cases:
print(subarray_sum([1, 1, 1], 2))  # Expected output: 2
print(subarray_sum([1, 2, 3], 3))  # Expected output: 2

# Testing the brute-force alternative:
print(subarray_sum_brute_force([1, 1, 1], 2))  # Expected output: 2
print(subarray_sum_brute_force([1, 2, 3], 3))  # Expected output: 2

# Time and Space Complexity Analysis:
#
# Optimal Prefix-Sum Solution (subarray_sum):
#   Time Complexity: O(n)
#     - We iterate through the list once and each dictionary operation is O(1) on average.
#
#   Space Complexity: O(n)
#     - In the worst case, the prefix_sums dictionary could store up to n distinct cumulative sums.
#
# Brute Force Solution (subarray_sum_brute_force):
#   Time Complexity: O(n^2)
#     - There are O(n^2) subarrays to consider.
#
#   Space Complexity: O(1)
#     - Only a few extra variables are used; no additional data structures proportional to n.
