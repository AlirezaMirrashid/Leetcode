"""
🔷 LeetCode 33: Search in Rotated Sorted Array

🧠 Task:
Given an integer array `nums` sorted in ascending order (with distinct values) that is possibly rotated at an unknown pivot,
and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not. The algorithm must run in O(log n)
runtime complexity.

-----------------------------------
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Explanation: The target 0 is found at index 4.

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Explanation: The target 3 is not in the array.

Example 3:
Input: nums = [1], target = 0
Output: -1

-----------------------------------
Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4 (all values unique)
    - nums is a sorted array that is possibly rotated.
    - -10^4 <= target <= 10^4
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        ✅ Optimal Approach using Binary Search (modified for rotated array)
        
        Approach:
          - Use binary search with two pointers, left and right.
          - Identify which half of the array is sorted.
          - If the target is within the sorted half, narrow the search to that half.
          - Otherwise, search the other half.
        
        ⏱ Time Complexity: O(log n)
        💾 Space Complexity: O(1)
        
        Args:
            nums (List[int]): A rotated sorted array of unique integers.
            target (int): The target value to search for.
        
        Returns:
            int: The index of the target if found, otherwise -1.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # Check if the left side is sorted
            if nums[left] <= nums[mid]:
                # If target is in the left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Otherwise, the right side is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    print("Example 1 Output:", sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
    print("Example 2 Output:", sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1
    print("Example 3 Output:", sol.search([1], 0))                      # Expected: -1

# ------------------------------------------------
# ✅ Time Complexity: O(log n), where n is the number of elements in the array.
# ✅ Space Complexity: O(1), since only a constant amount of extra space is used.
