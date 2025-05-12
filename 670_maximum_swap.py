"""
🔷 LeetCode 670: Maximum Swap (Medium)

🧠 Task:
You are given a non-negative integer `num`. You may swap two digits at most once to form the maximum valued number possible. Return that maximum number.

This version adds a third “scan-from-end” approach you suggested:
  - Keep track of the maximum digit seen so far as you move right-to-left,
    and the best pair of positions to swap.
"""

from typing import List

class Solution:
        def maximumSwap(self, num: int) -> int:
        """
        ✅ One-Pass + Last-Index Table (original optimal)

        Record the last occurrence of each digit, then for each position i scan from 9 down to
        current digit+1 to see if there is a bigger digit later to swap with.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(n)
        """
        """
        ✅ One-Pass + Last-Index Table (original optimal)

        Record the last occurrence of each digit, then for each position i scan from 9 down to
        current digit+1 to see if there is a bigger digit later to swap with.
        """
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        for i, ch in enumerate(digits):
            d = int(ch)
            for bigger in range(9, d, -1):
                if last.get(bigger, -1) > i:
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num

        def maximumSwapEndScan(self, num: int) -> int:
        """
        ✅ Scan-from-End Approach

        1. Convert number to digit list.
        2. Traverse from right to left, tracking:
             - `max_idx`: the index of the largest digit seen so far to the right.
             - Whenever digits[i] < digits[max_idx], record (i, max_idx) as the best swap.
        3. After the loop, if a beneficial swap was recorded, perform it.
        4. Return the resulting integer.

        ⏱ Time Complexity: O(n)
        💾 Space Complexity: O(n)
        """
        """
        ✅ Scan-from-End Approach

        1. Convert number to digit list.
        2. Traverse from right to left, tracking:
             - `max_idx`: the index of the largest digit seen so far to the right.
             - Whenever digits[i] < digits[max_idx], record (i, max_idx) as the best swap.
        3. After the loop, if a beneficial swap was recorded, perform it.
        4. Return the resulting integer.
        """
        digits = list(str(num))
        n = len(digits)
        max_idx = n - 1
        swap_i = -1
        swap_j = -1

        # Walk from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] > digits[max_idx]:
                # Found a new maximum to the right
                max_idx = i
            elif digits[i] < digits[max_idx]:
                # Found a place where swapping with max_idx would increase the number
                swap_i, swap_j = i, max_idx

        if swap_i != -1:
            digits[swap_i], digits[swap_j] = digits[swap_j], digits[swap_i]

        return int("".join(digits))

        def maximumSwapBruteForce(self, num: int) -> int:
        """
        ❌ Brute Force: try every possible single swap.

        ⏱ Time Complexity: O(n²)
        💾 Space Complexity: O(n)

        n is the number of digits (≤10), so O(n²) ≈ constant.
        """(self, num: int) -> int:
        """
        ❌ Brute Force: try every possible single swap.
        """
        s = list(str(num))
        n = len(s)
        best = num
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]
                best = max(best, int("".join(s)))
                s[i], s[j] = s[j], s[i]
        return best

# 🔸 Quick Tests
if __name__ == "__main__":
    sol = Solution()
    tests = [
        2736,    # → 7236
        9973,    # → 9973
        98368,   # → 98863
        1234,    # → 4231
    ]
    for num in tests:
        print(f"num = {num}")
        print("  last-index approach →", sol.maximumSwap(num))
        print("  end-scan approach   →", sol.maximumSwapEndScan(num))
        print("  brute-force approach→", sol.maximumSwapBruteForce(num))
        print("------------")
