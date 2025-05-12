"""
🔷 LeetCode 153 - Find Minimum in Rotated Sorted Array

🧠 Problem Summary:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

📌 Examples:

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0

Example 3:
Input: nums = [11,13,15,17]
Output: 11

💡 Intuition:
This is a classic binary search problem. The minimum value must be in the unsorted (rotated) half of the array.
If nums[mid] > nums[right], the min is in the right half.
Otherwise, it’s in the left half (including mid).
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be to the right of mid
                left = mid + 1
            else:
                # Minimum is at mid or to the left of mid
                right = mid

        return nums[left]

# 🔸 Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))        # ➞ 1
    print(sol.findMin([4,5,6,7,0,1,2]))    # ➞ 0
    print(sol.findMin([11,13,15,17]))      # ➞ 11
    print(sol.findMin([2,1]))              # ➞ 1

"""
🧠 Time and Space Complexity:

⏱ Time Complexity: O(log n)
- Standard binary search behavior by halving the search space.

💾 Space Complexity: O(1)
- Constant space used.
"""

