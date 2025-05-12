"""
🔷 LeetCode 31 - Next Permutation

🧠 Task:
Implement `nextPermutation`, which transforms a list of integers into its next lexicographically greater permutation.
If no such permutation exists (the array is in descending order), rearrange it to the lowest possible order (ascending).
The replacement must be done in place with only constant extra memory.

-----------------------------------
Example 1:
Input:  nums = [1,2,3]
After:  [1,3,2]

Example 2:
Input:  nums = [3,2,1]
After:  [1,2,3]

Example 3:
Input:  nums = [1,1,5]
After:  [1,5,1]

-----------------------------------
Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 100
"""

from typing import List
from itertools import permutations

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        ✅ Optimal Approach (In-Place, O(n) Time)

        1. Find the longest non-increasing suffix and identify its pivot just before the suffix.
        2. If the entire array is non-increasing, reverse it to the lowest order and return.
        3. Otherwise, find the rightmost successor to the pivot in the suffix.
        4. Swap the pivot with the successor.
        5. Reverse the suffix to get the next permutation.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(1)
        """
        # 1. Find pivot
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 2. Find rightmost successor to pivot
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. Swap pivot and successor
            nums[i], nums[j] = nums[j], nums[i]

        # 4. Reverse the suffix
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def nextPermutationBruteForce(self, nums: List[int]) -> None:
        """
        ❌ Brute Force Approach (Generate All Permutations)

        1. Generate all unique permutations, sort them lexicographically.
        2. Find the index of the current tuple.
        3. Replace nums in place with the next permutation (or the first if at end).

        ⏱ Time Complexity: O(n! * n log n) due to generating and sorting permutations.
        💾 Space Complexity: O(n! * n) to store all permutations.
        """
        perms = sorted(set(permutations(nums)))
        idx = perms.index(tuple(nums))
        next_perm = perms[(idx + 1) % len(perms)]
        for i in range(len(nums)):
            nums[i] = next_perm[i]


# 🔸 Sample Test Runs
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [1, 3, 2],
        [2, 3, 1]
    ]
    print("Optimal In-Place Approach:")
    for nums in test_cases:
        arr = nums.copy()
        sol.nextPermutation(arr)
        print(f"  before: {nums} → after: {arr}")

    print("\nBrute Force Approach:")
    for nums in test_cases:
        arr = nums.copy()
        sol.nextPermutationBruteForce(arr)
        print(f"  before: {nums} → after: {arr}")
