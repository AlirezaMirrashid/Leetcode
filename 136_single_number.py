"""
🔷 LeetCode 136 – Single Number

🧠 Problem Summary:
Given an integer array `nums` where every element appears twice except for one, find that single one.

✅ Constraints:
- Linear runtime O(n)
- Constant extra space O(1)

---

📌 Example:

Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1

---

💡 Solution 1 (XOR trick):
- XOR all numbers → pairs cancel out → only the single number remains.
- Properties:
    x ^ x = 0
    x ^ 0 = x

💡 Solution 2 (Brute force using HashMap — for reference only, violates space constraint):
- Count frequencies and return the key with count 1.
"""

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

    def singleNumberBruteForce(self, nums):
        from collections import Counter
        count = Counter(nums)
        for num, freq in count.items():
            if freq == 1:
                return num


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))      # 1
    print(sol.singleNumber([4, 1, 2, 1, 2])) # 4
    print(sol.singleNumber([1]))            # 1

"""
⏱ Time Complexity:
- XOR solution: O(n)
- Brute force: O(n)

💾 Space Complexity:
- XOR solution: O(1)
- Brute force: O(n) (for hash map)
"""
