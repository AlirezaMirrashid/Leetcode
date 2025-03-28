# LeetCode 347: Top K Frequent Elements
# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
#
# Description:
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
# Follow-up:
# Your algorithm's time complexity must be better than O(n log n).

from typing import List
from collections import Counter
import heapq


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Optimal Heap-based approach to find the k most frequent elements.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The number of most frequent elements to return.

    Returns:
        List[int]: A list containing the k most frequent elements.
    """
    # freq_map = Counter(nums)  # O(n) - Count frequency of elements
    freq_map = {}
    for num in nums:
        freq_map[num] = 1 + freq_map.get(num, 0)
    return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)  # O(n log k) - Get top k elements


# Bucket Sort Approach - O(n) Time Complexity
def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """
    Bucket Sort approach to find the k most frequent elements.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The number of most frequent elements to return.

    Returns:
        List[int]: A list containing the k most frequent elements.
    """
    # Step 1: Count frequency of each element
    freq_map = Counter(nums)  # O(n)

    # Step 2: Create buckets where index represents frequency
    n = len(nums)
    bucket = [[] for _ in range(n + 1)]  # O(n) space

    # Step 3: Fill buckets with numbers based on their frequency
    for num, freq in freq_map.items():
        bucket[freq].append(num)

    # Step 4: Collect the top k frequent elements from the highest frequency buckets
    result = []
    for i in range(n-1, -1, -1):  # O(n)
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result  # O(n) in worst case

    return result


# Brute-force Approach - O(n log n)
def top_k_frequent_brute_force(nums: List[int], k: int) -> List[int]:
    """
    Brute-force approach to find the k most frequent elements.

    Sorts the elements by frequency and returns the top k.

    Parameters:
        nums (List[int]): The list of integers.
        k (int): The number of most frequent elements to return.

    Returns:
        List[int]: A list containing the k most frequent elements.
    """
    freq_map = Counter(nums)  # O(n)
    sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    return [item[0] for item in sorted_items[:k]]  # O(k)


# Example test cases:
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # Expected output: [1,2]
print(top_k_frequent([1], 1))  # Expected output: [1]

# Testing the bucket sort solution:
print(top_k_frequent_bucket_sort([1, 1, 1, 2, 2, 3], 2))  # Expected output: [1,2]
print(top_k_frequent_bucket_sort([1], 1))  # Expected output: [1]

# Testing the brute-force alternative:
print(top_k_frequent_brute_force([1, 1, 1, 2, 2, 3], 2))  # Expected output: [1,2]
print(top_k_frequent_brute_force([1], 1))  # Expected output: [1]


# Time and Space Complexity Analysis:
#
# 1️⃣ Heap-Based Approach (top_k_frequent):
#   - Time Complexity: O(n log k)
#   - Space Complexity: O(n)
#
# 2️⃣ Bucket Sort Approach (top_k_frequent_bucket_sort):
#   - Time Complexity: O(n)
#   - Space Complexity: O(n)
#
# 3️⃣ Brute Force Approach (top_k_frequent_brute_force):
#   - Time Complexity: O(n log n)
#   - Space Complexity: O(n)
