# LeetCode 528: Random Pick with Weight
# Problem Link: https://leetcode.com/problems/random-pick-with-weight/
#
# Description:
# Given an array of positive integers w, where w[i] describes the weight of the ith index,
# implement the function pickIndex() which randomly picks an index in the range [0, w.length - 1]
# and returns it. The probability of picking an index i is proportional to w[i] / sum(w).
#
# Example 1:
# Input: w = [1]
# Output: [null, 0]
#
# Example 2:
# Input: w = [1, 3]
# Output: [null, 1, 1, 1, 1, 0]
# Explanation: The probability of picking index 0 is 1/(1+3)=0.25 and the probability of picking index 1 is 3/(1+3)=0.75.
#
# Constraints:
# 1 <= w.length <= 10^4
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10^4 times.

import random
import bisect
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        """
        Initializes the Solution object by precomputing the prefix sum of weights.
        This allows for efficient random selection in the pickIndex method.

        Parameters:
            w (List[int]): List of positive integers representing the weights.
        """
        self.prefix = []  # List to store the cumulative weights.
        self.total = 0  # Total sum of all weights.
        for weight in w:
            self.total += weight
            self.prefix.append(self.total)

    # def pickIndex(self) -> int:
    #     """
    #     Randomly picks an index in the range [0, len(w) - 1] with probability proportional to w[i].
    #
    #     Returns:
    #         int: The selected index.
    #     """
    #     # Pick a random integer in the range [1, total] (inclusive)
    #     target = random.randint(1, self.total)
    #     # Use binary search to find the leftmost index where prefix[i] is >= target.
    #     index = bisect.bisect_left(self.prefix, target)
    #     return index
    def pickIndex(self) -> int:
        # Pick a random number in the range [0, total] (inclusive)
        target = random.uniform(0, self.total)
        l, r = 0, len(self.prefix)
        while l < r:
            mid = (l + r) // 2
            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

# Brute Force Alternative (Not Recommended):
# One could imagine a brute-force solution that replicates each index w[i] times in a list and
# then randomly selects an index from that list. However, this approach is inefficient in both
# time and space, especially given the problem constraints.
#
# For example:
#
# class SolutionBruteForce:
#     def __init__(self, w: List[int]):
#         self.indices = []
#         for i, weight in enumerate(w):
#             self.indices.extend([i] * weight)
#
#     def pickIndex(self) -> int:
#         return random.choice(self.indices)
#
# This approach requires O(sum(w)) space and time for construction, which is impractical when
# w[i] can be as large as 10^5.

# Example test cases:
# Note: The output will be random, but the probabilities should match the weight distribution.
sol = Solution([1, 3])
# Running pickIndex() multiple times to observe the distribution.
print(sol.pickIndex())  # Expected: 0 with probability 0.25, 1 with probability 0.75
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())

# Time and Space Complexity Analysis:
#
# Time Complexity:
# - The __init__ method processes each element in w once, so it takes O(n) time, where n is the number of weights.
# - The pickIndex method uses binary search (bisect_left), which takes O(log n) time.
#
# Space Complexity:
# - The prefix array stores n elements, so it uses O(n) extra space.
