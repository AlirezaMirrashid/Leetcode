"""
🔷 LeetCode 169 – Majority Element

🧠 Problem Summary:
Given an integer array `nums`, return the element that appears more than ⌊n / 2⌋ times.

✅ Constraints:
- Array size ≥ 1
- Majority element always exists

---

📌 Example:

Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2

---

💡 Solution 1 (Boyer-Moore Voting Algorithm):
- Keep a candidate and a counter.
- Increment counter if the same, decrement if different.
- When counter drops to 0, switch candidate.
- Guaranteed to find majority because it appears > n/2 times.

💡 Solution 2 (Brute force with hashmap — uses extra space):
- Count frequencies and return the one with count > n//2.
"""

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

    def majorityElementBruteForce(self, nums):
        from collections import Counter
        count = Counter(nums)
        n = len(nums) // 2
        for num, freq in count.items():
            if freq > n:
                return num


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))       # 3
    print(sol.majorityElement([2,2,1,1,1,2,2])) # 2

"""
⏱ Time Complexity:
- Boyer-Moore: O(n)
- Brute force: O(n)

💾 Space Complexity:
- Boyer-Moore: O(1)
- Brute force: O(n) (for hash map)
"""
