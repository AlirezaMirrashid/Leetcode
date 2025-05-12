"""
🔷 LeetCode 1891 - Cutting Ribbons

🧠 Problem Summary:
You are given a list of ribbon lengths. You can cut them any way you want. 
Your task is to produce `k` ribbons, **all of the same length**.
Return the maximum length possible such that you can produce at least `k` ribbons of that length.

📘 Example:
Input: ribbons = [9, 7, 5], k = 3
Output: 5
Explanation:
- Cut 9 → 5 + 4
- Cut 7 → 5 + 2
- Keep 5
→ 3 ribbons of length 5

Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: Even 1-length ribbons can't make 22 ribbons total.

🎯 Goal: Maximize length such that we can make `k` ribbons of that length.

✅ Strategy:
Use **binary search** over ribbon length:
- Minimum length = 1
- Maximum length = max(ribbons)

Check at each midpoint if we can produce `k` ribbons of length `mid`
"""

from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut(length: int) -> bool:
            return sum(r // length for r in ribbons) >= k

        low, high = 1, max(ribbons)
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            if can_cut(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer


# 🔸 Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLength([9, 7, 5], 3))      # ➞ 5
    print(sol.maxLength([7, 5, 9], 4))      # ➞ 4
    print(sol.maxLength([5, 7, 9], 22))     # ➞ 0

"""
🧠 Time and Space Complexity:

⏱ Time Complexity: O(n * log(max(ribbons)))
- Binary search over length range: log(max(ribbons))
- Each check takes O(n) time

💾 Space Complexity: O(1) extra space (excluding input)
"""

