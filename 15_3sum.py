"""
🔷 LeetCode 15: 3Sum

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:
  - i, j, k are distinct indices,
  - nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
      The triplets that sum to zero are:
      [-1,  0,  1]
      [-1, -1,  2]

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation:
      No three numbers sum to zero.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation:
      Only one triplet (0,0,0) sums to zero, and duplicates are not allowed.

Constraints:
    3 ≤ nums.length ≤ 3000  
    -10⁵ ≤ nums[i] ≤ 10⁵  

We provide two methods:
 1. Brute-force triple loops (O(n³))  
 2. Sort + two-pointer scan (O(n²))  
"""

from typing import List

def threeSum_bruteforce(nums: List[int]) -> List[List[int]]:
    """
    Brute-force: try all triples, use a set to avoid duplicate triplets.
    
    Time Complexity: O(n³)
    Space Complexity: O(n³) for result in worst case (though duplicates are filtered)
    """
    n = len(nums)
    found = set()
    res = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = tuple(sorted((nums[i], nums[j], nums[k])))
                    if trip not in found:
                        found.add(trip)
                        res.append([trip[0], trip[1], trip[2]])
    return res

def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Optimal: sort and for each index use two-pointer to find complementary pairs.
    
    Time Complexity: O(n²)
    Space Complexity: O(log n) or O(n) depending on sort implementation
    """
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-2):
        # skip duplicate first elements
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        lo, hi = i+1, n-1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == target:
                res.append([nums[i], nums[lo], nums[hi]])
                # skip duplicates for lo and hi
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi+1]:
                    hi -= 1
            elif s < target:
                lo += 1
            else:
                hi -= 1
    return res

# ------------- Sample tests -------------
if __name__ == "__main__":
    test_cases = [
        ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
        ([0,1,1], []),
        ([0,0,0], [[0,0,0]]),
        ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]]),
        ([], []),
        ([1,-1,-1,0], [[-1,0,1]]),
    ]
    for nums, expected in test_cases:
        out_bf = threeSum_bruteforce(nums[:])
        out_opt = threeSum(nums[:])
        # sort inner lists and outer list for comparison
        def norm(lst):
            return sorted([tuple(trip) for trip in lst])
        print(f"nums = {nums}")
        print(" Brute :", norm(out_bf))
        print("Optimal:", norm(out_opt))
        print("Expected:", norm(expected))
        print("-----")

"""
✅ Complexity Summary:
- Brute-force:
    Time:  O(n³)
    Space: O(n³) (result storage)

- Sort + two-pointer:
    Time:  O(n²)
    Space: O(log n) (in-place sort) or O(n)
"""
