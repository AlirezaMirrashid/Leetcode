"""
🔷 LeetCode 53: Maximum Subarray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum = 1.

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4

Follow up: 
    1) O(n) solution (Kadane’s algorithm).  
    2) Divide and conquer approach.

We’ll implement three methods:
 1. Brute-force      – O(n²) time  
 2. Kadane’s (DP)    – O(n) time  
 3. Divide & conquer – O(n log n) time  
"""

from typing import List

def max_subarray_bruteforce(nums: List[int]) -> int:
    """
    Brute-force: evaluate sum of every subarray.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    max_sum = nums[0]
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += nums[j]
            max_sum = max(max_sum, current)
    return max_sum

def max_subarray_kadane(nums: List[int]) -> int:
    """
    Kadane's algorithm (dynamic programming in O(n)):
    Track current subarray sum ending here, reset to 0 if negative.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_sum = nums[0]
    current = 0
    for x in nums:
        # if current is negative, start new subarray at x
        current = max(x, current + x)
        max_sum = max(max_sum, current)
    return max_sum

def max_subarray_divide_conquer(nums: List[int]) -> int:
    """
    Divide and conquer: split array, compute best in left, right, crossing middle.
    Time Complexity: O(n log n)
    Space Complexity: O(log n) recursion depth
    """
    def helper(l: int, r: int) -> int:
        if l == r:
            return nums[l]
        m = (l + r) // 2
        # best left, best right, best crossing
        left_max = helper(l, m)
        right_max = helper(m+1, r)
        
        # compute crossing sum
        left_sum = float('-inf')
        s = 0
        for i in range(m, l-1, -1):
            s += nums[i]
            left_sum = max(left_sum, s)
        right_sum = float('-inf')
        s = 0
        for j in range(m+1, r+1):
            s += nums[j]
            right_sum = max(right_sum, s)
        
        cross_max = left_sum + right_sum
        return max(left_max, right_max, cross_max)
    
    return helper(0, len(nums)-1)

# ------------- Sample tests -------------
if __name__ == "__main__":
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
        ([-1,-2,-3], -1),
        ([0, -3, 1, 2, -1, 2], 4),  # subarray [1,2,-1,2]
    ]
    for nums, expected in test_cases:
        print("nums =", nums)
        print(" Brute-force      ->", max_subarray_bruteforce(nums), " expected", expected)
        print(" Kadane’s (O(n))  ->", max_subarray_kadane(nums),       " expected", expected)
        print(" Divide & Conquer ->", max_subarray_divide_conquer(nums), " expected", expected)
        print("---")

"""
✅ Time & Space Complexity Summary:

1. Brute-force:
   - Time:  O(n^2)
   - Space: O(1)

2. Kadane’s Algorithm:
   - Time:  O(n)
   - Space: O(1)

3. Divide & Conquer:
   - Time:  O(n log n)
   - Space: O(log n)   (recursion stack)
"""
