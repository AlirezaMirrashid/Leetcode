"""
🔷 LeetCode 


A conveyor belt has packages that must be shipped from one port to another within `days` days.

- The iᵗʰ package has weight `weights[i]`.
- Each day, you load the ship with packages in the given order, without exceeding the ship’s capacity.
- You must ship all packages within `days` days.

Return the **minimum** ship capacity that allows all packages to be shipped within `days` days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation:
      Day 1: 1,2,3,4,5   (sum=15)
      Day 2: 6,7         (sum=13)
      Day 3: 8           (sum=8)
      Day 4: 9           (sum=9)
      Day 5: 10          (sum=10)
    Capacity 15 is the smallest that works.

Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6
    Explanation:
      Day 1: 3,2       (sum=5)
      Day 2: 2,4       (sum=6)
      Day 3: 1,4       (sum=5)

Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3
    Explanation:
      Day 1: 1
      Day 2: 2
      Day 3: 3
      Day 4: 1,1

Constraints:
    1 ≤ days ≤ weights.length ≤ 5·10⁴
    1 ≤ weights[i] ≤ 500

We present two approaches:
 1. Brute-force scan capacities              – O(n·S) time, where S = sum(weights)
 2. Binary search on capacity + greedy check – O(n·log S) time
"""

from typing import List

def can_ship(weights: List[int], days: int, capacity: int) -> bool:
    """
    Greedy check: simulate shipping with given capacity.
    Return True if we can ship within 'days'.
    """
    required_days = 1
    current_load = 0
    for w in weights:
        # if single weight > capacity, impossible
        if w > capacity:
            return False
        if current_load + w <= capacity:
            current_load += w
        else:
            required_days += 1
            current_load = w
            if required_days > days:
                return False
    return True

def shipWithinDays_bruteforce(weights: List[int], days: int) -> int:
    """
    Brute-force: try every capacity from max(weights) up to sum(weights).
    
    Time Complexity: O(n * S), where S = sum(weights).
    Space Complexity: O(1)
    """
    low = max(weights)
    high = sum(weights)
    for cap in range(low, high+1):
        if can_ship(weights, days, cap):
            return cap
    return high  # fallback

def shipWithinDays(weights: List[int], days: int) -> int:
    """
    Binary search the minimum feasible capacity.

    Time Complexity: O(n · log S), where S = sum(weights).
    Space Complexity: O(1)
    """
    low = max(weights)
    high = sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship(weights, days, mid):
            high = mid
        else:
            low = mid + 1
    return low

# ------------- Sample tests -------------
if __name__ == "__main__":
    tests = [
        ([1,2,3,4,5,6,7,8,9,10], 5, 15),
        ([3,2,2,4,1,4], 3, 6),
        ([1,2,3,1,1], 4, 3),
        ([10,10,10], 1, 30),
        ([10,10,10], 3, 10),
    ]
    for weights, days, expected in tests:
        print("weights =", weights, "days =", days)
        print(" Brute-force      ->", shipWithinDays_bruteforce(weights, days), "expected", expected)
        print(" Binary-search    ->", shipWithinDays(weights, days),         "expected", expected)
        print("---")

"""
✅ Complexity Summary:

1. Brute-force scan:
   - Time:  O(n · S)   where S = sum(weights)
   - Space: O(1)

2. Binary search + greedy check:
   - Time:  O(n · log S)
   - Space: O(1)
"""
