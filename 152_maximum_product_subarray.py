
"""
🔵 LeetCode 152. Maximum Product Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the largest product, and return the product.

-----------------------------------
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: The subarray [2,3] has the maximum product = 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result is 0 because the only non-zero product subarrays are [-2], [0], and [-1].

-----------------------------------
Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of `nums` is guaranteed to fit in a 32-bit integer.
"""

from typing import List

def max_product(nums: List[int]) -> int:
    """
    ✅ Optimal Solution (Dynamic Programming)

    Idea:
    - Use two variables to track the max and min products ending at current index.
    - At each number, max can become min if number is negative (and vice versa).
    - Result is the maximum of all max_so_far values.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_so_far = min_so_far = result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        if curr < 0:
            max_so_far, min_so_far = min_so_far, max_so_far  # flip due to negative

        max_so_far = max(curr, curr * max_so_far)
        min_so_far = min(curr, curr * min_so_far)
        result = max(result, max_so_far)

    return result

def max_product_2(nums: List[int]) -> int:
    """
    ✅ Optimal Solution (Dynamic Programming)

    Idea:
    - Use two variables to track the max and min products ending at current index.


    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    res = max(nums)
    curMin, curMax = 1,1
    for n in nums:
        if n == 0:
            curMin, curMax = 1,1
            continue
        tmp = curMax*n
        curMax = max(n*curMax, n*curMin, n)
        curMin = min(tmp, n*curMin, n)
        res = max(res,curMax)
    return res

def max_product_brute(nums: List[int]) -> int:
    """
    ❌ Brute Force Solution

    Idea:
    - Try every possible subarray and compute product.
    - Inefficient for large input.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    max_product = nums[0]
    
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            max_product = max(max_product, prod)

    return max_product


# ✅ Sample Test Cases
if __name__ == "__main__":
    nums1 = [2, 3, -2, 4]
    print("Optimal:", max_product(nums1))  # Output: 6
    print("Brute Force:", max_product_brute(nums1))  # Output: 6

    nums2 = [-2, 0, -1]
    print("Optimal:", max_product(nums2))  # Output: 0
    print("Brute Force:", max_product_brute(nums2))  # Output: 0

    nums3 = [-2, 3, -4]
    print("Optimal:", max_product(nums3))  # Output: 24
    print("Brute Force:", max_product_brute(nums3))  # Output: 24





