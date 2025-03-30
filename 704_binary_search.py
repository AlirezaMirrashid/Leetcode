"""
🔵 LeetCode 704: Binary Search

You are given an array of integers `nums`, sorted in ascending order, and an integer `target`.
Write a function to search for `target` in `nums`. If the target exists, return its index; 
otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

-----------------------------------
Example 1:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 
    The number 9 exists at index 4 in the array.

Example 2:
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 
    The number 2 does not exist in the array.

-----------------------------------

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All integers in nums are unique.
    - nums is sorted in ascending order.
"""

from typing import List

def binarySearch(nums: List[int], target: int):
    """
    This function implements binary search on a sorted array `nums` to find the index of `target`.
    If the `target` exists in `nums`, it returns its index. Otherwise, it returns -1.
    
    The algorithm uses the binary search approach, which reduces the search space by half at each step.
    
    Time Complexity: O(log n), where n is the length of the input array. The search space is halved at each step.
    Space Complexity: O(1), as the function uses a constant amount of extra space.
    
    Args:
        nums (List[int]): The list of integers (sorted in ascending order).
        target (int): The integer value to search for in the list.
    
    Returns:
        int: The index of the target in the list, or -1 if not found.
    """
    
    # Initialize pointers for the binary search
    left, right = 0, len(nums) - 1
    
    # Perform binary search
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        # Check if the target is at mid index
        if nums[mid] == target:
            return mid
        # If target is smaller, ignore the right half
        elif nums[mid] > target:
            right = mid - 1
        # If target is larger, ignore the left half
        else:
            left = mid + 1
    
    # If target is not found, return -1
    return -1


# Sample Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(binarySearch(nums1, target1))  # Expected: 4
    
    # Test Case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(binarySearch(nums2, target2))  # Expected: -1
    
    # Test Case 3 (Target is at the start)
    nums3 = [-10, 0, 3, 5, 9, 12]
    target3 = -10
    print(binarySearch(nums3, target3))  # Expected: 0
    
    # Test Case 4 (Target is at the end)
    nums4 = [-10, 0, 3, 5, 9, 12]
    target4 = 12
    print(binarySearch(nums4, target4))  # Expected: 5

# ------------------------------------------------
# ✅ Time Complexity: O(log n), as the search space is halved at each step of the binary search.
# ✅ Space Complexity: O(1), since only a constant amount of space is used for pointers and variables.
