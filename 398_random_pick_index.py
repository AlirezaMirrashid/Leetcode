"""
🔷 LeetCode 398: Random Pick Index

🧠 Task:
Given an integer array `nums` with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.
If there are multiple valid indices, each index should have an equal probability of being returned.

Implement the `Solution` class:
  - __init__(nums): Initializes the object with the array nums.
  - pick(target): Picks a random index i from nums such that nums[i] == target.

-----------------------------------
Example:
Input:
  nums = [1, 2, 3, 3, 3]
  pick(3) → It should return one of indices: 2, 3, or 4 randomly.
  pick(1) → Should return index 0, because it's the only occurrence.
Output:
  [null, 4, 0, 2]   (Output order may vary as long as the returned index is correct and random.)

-----------------------------------
Constraints:
    - 1 <= nums.length <= 2 * 10^4
    - -2^31 <= nums[i] <= 2^31 - 1
    - target is an integer from nums.
    - At most 10^4 calls will be made to pick.
"""

import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        """
        ✅ Preprocessing using dictionary mapping
        
        Approach:
          - Traverse the input array `nums` once.
          - Build a dictionary mapping each number to a list of its indices.
          - This allows picking a random index for any target in O(1) time.
        
        ⏱ Time Complexity: O(n), where n is the number of elements in nums.
        💾 Space Complexity: O(n)
        
        Args:
            nums (List[int]): The input array of integers.
        """
        self.mapping = {}
        for index, num in enumerate(nums):
            if num not in self.mapping:
                self.mapping[num] = []
            self.mapping[num].append(index)
        # Store the nums list, in case we want to use an alternative solution (reservoir sampling) later.
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Returns a random index such that self.nums[index] == target.
        
        Approach:
          - Using the dictionary mapping from initialization, select a random index from the list.
        
        ⏱ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        
        Args:
            target (int): The target number to find.
        
        Returns:
            int: A random index i such that self.nums[i] == target.
        """
        return random.choice(self.mapping[target])
    
    # Alternative solution using reservoir sampling
    def pickReservoir(self, target: int) -> int:
        """
        ❌ Alternative: Reservoir Sampling Approach (Without extra storage for mapping)
        
        This method iterates through the entire array and selects a random index among the indices where
        self.nums[i] == target. Each valid index is chosen with equal probability.
        
        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(1)
        
        Args:
            target (int): The target number to find.
        
        Returns:
            int: A random index i such that self.nums[i] == target.
        """
        count = 0
        result = -1
        for i, num in enumerate(self.nums):
            if num == target:
                # Increase count of found occurrences, and randomly choose current index with probability 1/count
                count += 1
                if random.randint(1, count) == 1:
                    result = i
        return result


# 🔸 Sample Test Runs
if __name__ == "__main__":
    # Example: nums = [1,2,3,3,3]
    nums = [1, 2, 3, 3, 3]
    sol = Solution(nums)
    
    # Test using dictionary mapping solution
    print("Using dictionary mapping approach:")
    print("pick(3):", sol.pick(3))  # Expected output: One of 2, 3, or 4 randomly.
    print("pick(1):", sol.pick(1))  # Expected output: 0
    
    # Test using reservoir sampling approach
    print("\nUsing reservoir sampling approach:")
    print("pickReservoir(3):", sol.pickReservoir(3))  # Expected output: One of 2, 3, or 4 randomly.
    print("pickReservoir(1):", sol.pickReservoir(1))  # Expected output: 0

# ------------------------------------------------
# ✅ Time Complexity:
#      - Dictionary Mapping Approach: O(1) per call to pick
#      - Reservoir Sampling Approach: O(n) per call to pickReservoir
# ✅ Space Complexity: O(n) for storing the mapping, O(1) for reservoir sampling aside from input storage.
