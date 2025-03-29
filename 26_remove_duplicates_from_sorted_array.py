"""
🔵 LeetCode 26: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k. To get accepted, you need to do the following:
  - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
  - The remaining elements of nums are not important.
  - Return k.

Custom Judge:
  The judge will test your solution with the following code:
      int[] nums = [...]; // Input array
      int[] expectedNums = [...]; // The expected answer with correct length
      
      int k = removeDuplicates(nums); // Calls your implementation
      
      assert k == expectedNums.length;
      for (int i = 0; i < k; i++) {
          assert nums[i] == expectedNums[i];
      }
  If all assertions pass, then your solution will be accepted.

-----------------------------------
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k.

-----------------------------------
Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.
"""

from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    ✅ Optimal Two-Pointer Approach
    
    Approach:
      - Use two pointers: one (i) for the position of the last unique element,
        and the other (j) for scanning the array.
      - For each element at index j, if it differs from the element at i,
        increment i and update nums[i] with nums[j].
      - The number of unique elements is i + 1.
    
    Parameters:
        nums (List[int]): The sorted list of integers with possible duplicates.
    
    Returns:
        int: The number of unique elements after in-place removal of duplicates.
    """
    if not nums:
        return 0
    
    i = 0  # Pointer to the position of the last unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
    
    # i = 1  # Pointer to the position of the last unique element
    # for j in range(1, len(nums)):
        # if nums[j] != nums[j-1]:
            # nums[i] = nums[j]
            # i += 1
    # return i

# Sample Test Cases
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 1, 2]
    k1 = remove_duplicates(nums1)
    print("Example 1 Output:", k1, nums1[:k1])  # Expected k1 = 2, nums1[:2] = [1, 2]
    
    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = remove_duplicates(nums2)
    print("Example 2 Output:", k2, nums2[:k2])  # Expected k2 = 5, nums2[:5] = [0, 1, 2, 3, 4]

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n = len(nums)
# ✅ Space Complexity: O(1)
