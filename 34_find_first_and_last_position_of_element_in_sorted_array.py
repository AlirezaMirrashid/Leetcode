"""
🔷 LeetCode 34 - Find First and Last Position of Element in Sorted Array

🧠 Task:
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending 
positions of a given target value. If target is not found, return [-1, -1].

⚙️ Requirements:
- The algorithm must run in O(log n) runtime complexity.

-----------------------------------
Example 1:
Input:  nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Explanation: The target value 8 appears first at index 3 and last at index 4.

Example 2:
Input:  nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Explanation: The target value 6 is not present in the array.

Example 3:
Input:  nums = [], target = 0
Output: [-1,-1]
Explanation: The array is empty so the target is not found.

-----------------------------------
Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - nums is sorted in non-decreasing order.
    - -10^9 <= target <= 10^9
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Uses binary search to find the first and last positions of `target` in the sorted list `nums`.

        Approach:
          - First binary search finds the leftmost (first) occurrence of target.
          - Second binary search finds the rightmost (last) occurrence of target.
          - If target is not found, return [-1, -1].

        """
        
        def binarySearchLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                if nums[mid] == target:
                    index = mid
            return index
        
        def binarySearchRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    index = mid
            return index
        
        left_index = binarySearchLeft(nums, target)
        if left_index == -1:
            return [-1, -1]
        right_index = binarySearchRight(nums, target)
        return [left_index, right_index]

    def searchRangeBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        ❌ Brute Force Approach
        
        This method iterates through the list to find the first and last occurrence of target.
        
        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(1)
        
        Args:
            nums (List[int]): Sorted list of integers.
            target (int): The target value.
        
        Returns:
            List[int]: A list containing the starting and ending positions of target in nums.
        """
        first, last = -1, -1
        for i, num in enumerate(nums):
            if num == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]

# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1:
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    print("Example 1 Output:", sol.searchRange(nums1, target1))  # Expected: [3,4]
    
    # Example 2:
    nums2 = [5,7,7,8,8,10]
    target2 = 6
    print("Example 2 Output:", sol.searchRange(nums2, target2))  # Expected: [-1, -1]
    
    # Example 3:
    nums3 = []
    target3 = 0
    print("Example 3 Output:", sol.searchRange(nums3, target3))  # Expected: [-1, -1]
    
# ------------------------------------------------
# ✅ Time Complexity: O(log n), as we perform binary search twice.
# ✅ Space Complexity: O(1), since only a constant extra space is used.
