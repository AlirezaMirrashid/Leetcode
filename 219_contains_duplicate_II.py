"""
🔵 LeetCode 219: Contains Duplicate II

Given an integer array `nums` and an integer `k`, return true if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k. Otherwise, return false.

-----------------------------------
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] == nums[3] and abs(0 - 3) = 3 <= 3.

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: nums[2] == nums[3] and abs(2 - 3) = 1 <= 1.

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

-----------------------------------
Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - 0 <= k <= 10^5
"""

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Optimal Approach using a dictionary to store the last seen index of each number.

    Approach:
      - Iterate through the array while maintaining a dictionary `last_seen` that maps each number to its last index.
      - For each number, if it exists in `last_seen` and the difference between the current index and the stored index 
        is less than or equal to k, return True.
      - Otherwise, update the dictionary with the current index.
      - If no such pair is found, return False.

    Time Complexity: O(n), where n is the length of nums.
    Space Complexity: O(n) in the worst case.
    
    Args:
        nums (List[int]): The list of integers.
        k (int): The maximum allowed index difference.
    
    Returns:
        bool: True if there are two indices i and j such that nums[i] == nums[j] and abs(i - j) <= k, otherwise False.
    """
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False

def containsNearbyDuplicate_set(nums: List[int], k: int) -> bool:
    """
    Alternative Approach using a sliding window set.

    Approach:
      - Maintain a set to store at most k elements (the current sliding window).
      - Iterate through the list; if the current number is already in the set, return True.
      - Otherwise, add the current number to the set.
      - If the window size exceeds k, remove the element that is now out of range.
      - Return False if no duplicates are found within the window.
    
    Time Complexity: O(n), where n is the length of nums.
    Space Complexity: O(k), where k is the maximum window size.
    
    Args:
        nums (List[int]): The list of integers.
        k (int): The maximum allowed index difference.
    
    Returns:
        bool: True if a duplicate exists within k indices, otherwise False.
    """
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False

# Sample Test Cases
if __name__ == "__main__":
    # Example 1:
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print("Dictionary Approach, Example 1 Output:", containsNearbyDuplicate(nums1, k1))  # Expected: True

    # Example 2:
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print("Dictionary Approach, Example 2 Output:", containsNearbyDuplicate(nums2, k2))  # Expected: True

    # Example 3:
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print("Dictionary Approach, Example 3 Output:", containsNearbyDuplicate(nums3, k3))  # Expected: False

    # Testing the alternative sliding window approach:
    print("Sliding Window Approach, Example 1 Output:", containsNearbyDuplicate_set(nums1, k1))  # Expected: True
    print("Sliding Window Approach, Example 2 Output:", containsNearbyDuplicate_set(nums2, k2))  # Expected: True
    print("Sliding Window Approach, Example 3 Output:", containsNearbyDuplicate_set(nums3, k3))  # Expected: False

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the length of nums.
# ✅ Space Complexity: 
#     - Dictionary Approach: O(n) in the worst case.
#     - Sliding Window Approach: O(k), where k is the maximum allowed window size.
