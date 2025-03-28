# LeetCode 215: Kth Largest Element in an Array
# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Description:
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
#
# Example 2:
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
#
# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
# Can you solve it without sorting?

import heapq
from typing import List


def kth_largest(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in the list `nums` using a min-heap.

    The idea is to maintain a min-heap of size k. For each number in nums:
      - If the heap size is less than k, we push the number onto the heap.
      - Otherwise, if the number is greater than the smallest element (heap[0]),
        we remove the smallest element and push the current number onto the heap.

    After processing all numbers, the root of the min-heap (heap[0]) is the kth largest element.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The kth largest element to find.

    Returns:
        int: The kth largest element in nums.
    """
    # Edge case: if there are fewer elements than k, return None.
    if len(nums) < k:
        return None

    min_heap = []  # Initialize an empty min-heap.

    for num in nums:
        if len(min_heap) < k:
            # If the heap has less than k elements, add the current number.
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            # If the current number is larger than the smallest in the heap,
            # remove the smallest and add the current number.
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # The root of the min-heap is the kth largest element.
    return min_heap[0]


# Brute Force Alternative: Sorting Approach
def kth_largest_sort(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element using sorting.

    The list is sorted in descending order, and the element at index k-1 is returned.
    This approach has higher time complexity (O(n log n)) and is not optimal for large inputs.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The kth largest element to find.

    Returns:
        int: The kth largest element in nums.
    """
    # Sort the array in descending order and return the kth element.
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[k - 1]


# Example test cases:
print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4

# Testing the brute-force sorting approach:
print(kth_largest_sort([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(kth_largest_sort([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4

# Time and Space Complexity Analysis:
#
# Optimal Heap-based Solution (kth_largest):
#   Time Complexity: O(n log k)
#     - Each of the n elements is pushed or popped from the heap, which takes O(log k) time.
#
#   Space Complexity: O(k)
#     - The heap stores at most k elements.
#
# Brute Force Sorting Approach (kth_largest_sort):
#   Time Complexity: O(n log n)
#     - Sorting the entire array takes O(n log n) time.
#
#   Space Complexity: O(n)
#     - Sorting may require O(n) space depending on the algorithm.
