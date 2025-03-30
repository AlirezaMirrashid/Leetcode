"""
🔵 LeetCode 88: Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate
this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n
elements are set to 0 and should be ignored. nums2 has a length of n.

-----------------------------------
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1].
-----------------------------------

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - 1 <= m + n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9
"""

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted arrays (nums1 and nums2) into one sorted array, where nums1 has enough space to accommodate both.
    
    Approach:
      - Start with two pointers: one for the end of the first m elements in nums1 (l1) and one for the end of nums2 (l2).
      - Fill nums1 starting from the end (from the largest available index).
      - Compare the elements from the back of nums1 and nums2, placing the larger one in the last available slot in nums1.
      - Continue this process until all elements from nums2 are placed into nums1.
      - If there are any remaining elements in nums2, place them in nums1.
      - If there are remaining elements in nums1, they are already in place.

    Time Complexity: O(m + n), where m and n are the lengths of nums1 and nums2.
    Space Complexity: O(1), as we are modifying nums1 in place.

    Parameters:
        nums1 (List[int]): The first sorted array, with enough space to accommodate nums2.
        m (int): The number of valid elements in nums1.
        nums2 (List[int]): The second sorted array.
        n (int): The number of valid elements in nums2.
    
    Returns:
        None: The function modifies nums1 in place.
    """
    l1, l2, l = m - 1, n - 1, m + n - 1  # Start from the end of nums1, nums2, and nums1's total space.

    # Merge nums1 and nums2 while both arrays have elements left
    while l1 >= 0 and l2 >= 0:
        if nums1[l1] > nums2[l2]:
            nums1[l] = nums1[l1]
            l1 -= 1
        else:
            nums1[l] = nums2[l2]
            l2 -= 1
        l -= 1

    # If there are any remaining elements in nums2, place them in nums1
    while l2 >= 0:
        nums1[l] = nums2[l2]
        l2 -= 1
        l -= 1

# Sample Test Cases
if __name__ == "__main__":
    nums1_1 = [1, 2, 3, 0, 0, 0]
    nums2_1 = [2, 5, 6]
    merge(nums1_1, 3, nums2_1, 3)
    print("Example 1 Output:", nums1_1)  # Expected: [1, 2, 2, 3, 5, 6]

    nums1_2 = [1]
    nums2_2 = []
    merge(nums1_2, 1, nums2_2, 0)
    print("Example 2 Output:", nums1_2)  # Expected: [1]

    nums1_3 = [0]
    nums2_3 = [1]
    merge(nums1_3, 0, nums2_3, 1)
    print("Example 3 Output:", nums1_3)  # Expected: [1]

# ------------------------------------------------
# ✅ Time Complexity: O(m + n), where m and n are the number of elements in nums1 and nums2, respectively.
# ✅ Space Complexity: O(1), as we are modifying nums1 in place.
