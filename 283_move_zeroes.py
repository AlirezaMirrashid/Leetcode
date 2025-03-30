"""
🔵 LeetCode 283: Move Zeroes

You are given an integer array `nums`, and your task is to move all the zeroes in the array to the end 
while maintaining the relative order of the non-zero elements. 

You must do this in-place without making a copy of the array.

-----------------------------------
Example 1:
Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Explanation: 
    Initially, nums = [0, 1, 0, 3, 12]
    After moving zeroes to the end, nums = [1, 3, 12, 0, 0]

Example 2:
Input: nums = [0]
Output: [0]
Explanation: 
    There is only one zero, so the array remains unchanged.

-----------------------------------

Constraints:
    - 1 <= nums.length <= 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List

def moveZeroes(nums: List[int]):
    """
    This function moves all zeroes in the input array `nums` to the end, while maintaining the relative order of non-zero elements.
    
    The algorithm uses a two-pointer technique to swap zeroes with non-zero elements in-place.
    

    Args:
        nums (List[int]): The list of integers where zeroes should be moved to the end.
    
    Returns:
        List[int]: The input list modified such that all zeroes are moved to the end.
    """
    
    # Initialize two pointers
    left, right = 0, 0  # left pointer tracks where to place non-zero elements
    
    # Traverse through the array with the right pointer
    while right < len(nums):
        if nums[right]:  # If the current element is not zero
            # Swap the elements at left and right
            nums[left], nums[right] = nums[right], nums[left]
            left += 1  # Increment left to track the next position for non-zero element
        right += 1  # Always increment right to continue through the array
    
    return nums  # Return the modified list


# Sample Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 0, 3, 12]
    print(moveZeroes(nums1))  # Expected: [1, 3, 12, 0, 0]
    
    # Test Case 2
    nums2 = [0]
    print(moveZeroes(nums2))  # Expected: [0]
    
    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(moveZeroes(nums3))  # Expected: [1, 2, 3, 4, 5] (no zeroes in the list)
    
    # Test Case 4
    nums4 = [0, 0, 0, 1, 2, 3]
    print(moveZeroes(nums4))  # Expected: [1, 2, 3, 0, 0, 0]
    
# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the length of the input array. The array is traversed only once.
# ✅ Space Complexity: O(1), since the modification is done in place without using extra space.
