"""
🔵 LeetCode 80. Remove Duplicates from Sorted Array II

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears **at most twice**. The relative order of the elements should be kept the same.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Return `k` after placing the final result in the first `k` slots of `nums`.

-----------------------------------
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: The first 5 elements after removing excess duplicates are [1,1,2,2,3].

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]

-----------------------------------
Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order
"""

from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    ✅ Optimal In-Place Solution (Two Pointers)

    Idea:
    - Use two pointers: `i` is the place to insert next valid number.
    - Allow each element to appear at most twice.
    - If current number is not equal to nums[i-2], it's safe to insert.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(nums) <= 2:
        return len(nums)
    
    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
    return i


def remove_duplicates_brute(nums: List[int]) -> int:
    """
    ❌ Brute Force Solution (Not In-Place Friendly)

    Idea:
    - Use extra space (not allowed by problem constraints).
    - Count occurrences and manually build the allowed list.

    Time Complexity: O(n)
    Space Complexity: O(n) ❌ violates space constraint
    """
    from collections import defaultdict
    count = defaultdict(int)
    result = []

    for num in nums:
        if count[num] < 2:
            result.append(num)
            count[num] += 1

    # Modify original array to match in-place requirement for judge
    for i in range(len(result)):
        nums[i] = result[i]
    
    return len(result)


# ✅ Sample Test Cases
if __name__ == "__main__":
    nums1 = [1,1,1,2,2,3]
    k1 = remove_duplicates(nums1)
    print("Optimal:", k1, ", nums:", nums1[:k1])  # [1,1,2,2,3]

    nums2 = [0,0,1,1,1,1,2,3,3]
    k2 = remove_duplicates(nums2)
    print("Optimal:", k2, ", nums:", nums2[:k2])  # [0,0,1,1,2,3,3]

    nums3 = [1,1,1,1]
    k3 = remove_duplicates(nums3)
    print("Optimal:", k3, ", nums:", nums3[:k3])  # [1,1]

    # Brute Force (not valid for submission but useful to compare)
    nums4 = [1,1,1,2,2,3]
    k4 = remove_duplicates_brute(nums4)
    print("Brute Force:", k4, ", nums:", nums4[:k4])  # [1,1,2,2,3]
