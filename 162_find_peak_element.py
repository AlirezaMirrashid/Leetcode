"""
🔵 LeetCode 162: Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is 
always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

-----------------------------------
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 1 where the peak element is 2, 
or index 5 where the peak element is 6.

-----------------------------------
Constraints:
    - 1 <= nums.length <= 1000
    - -2^31 <= nums[i] <= 2^31 - 1
    - nums[i] != nums[i + 1] for all valid i.
"""

from typing import List

def findPeakElement(nums: List[int]) -> int:
    """
    Finds a peak element in the given array and returns its index.
    
    Approach:
      - Uses Binary Search to achieve O(log n) time complexity.
      - If nums[mid] > nums[mid + 1], the peak is on the left side, move left.
      - Else, the peak is on the right side, move right.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        nums (List[int]): A list of integers.
    
    Returns:
        int: The index of a peak element.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak must be in the left half (including mid)
            right = mid
        else:
            # Peak must be in the right half (excluding mid)
            left = mid + 1

    return left  # left == right, which is the peak index


# Sample Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Peak index in {nums1}: {findPeakElement(nums1)}")  # Expected output: 2

    # Test Case 2
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print(f"Peak index in {nums2}: {findPeakElement(nums2)}")  # Expected output: 1 or 5

    # Test Case 3
    nums3 = [10, 20, 15, 2, 23, 90, 67]
    print(f"Peak index in {nums3}: {findPeakElement(nums3)}")  # Expected output: 1 or 5

# ------------------------------------------------
# ✅ Time Complexity: O(log n), due to binary search.
# ✅ Space Complexity: O(1), as no extra space is used.
