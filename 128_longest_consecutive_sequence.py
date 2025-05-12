"""
🔷 LeetCode 128 – Longest Consecutive Sequence

🧠 Problem Summary:
Given an unsorted array of integers `nums`, return the length of the longest sequence of consecutive integers.

You must write an algorithm with O(n) time complexity.

✅ Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

---

📌 Examples:

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive sequence is [1,2,3,4].

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6,7,8].

Example 3:
Input: nums = [1,0,1,2]
Output: 3
Explanation: The longest consecutive sequence is [0,1,2].

---

💡 Core Idea:
Use a hash set to achieve O(n):
1. Insert all numbers into a set.
2. For each number, if it's the start of a sequence (num-1 not in set), iterate forward counting num+1, num+2, … until break.
3. Track the maximum length found.

This ensures each number is visited O(1) times overall.

---

🐍 Python Implementation:
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start counting if `num` is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1
                # count consecutive numbers
                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest


# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))            # 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))        # 9
    print(sol.longestConsecutive([1,0,1,2]))                   # 3
    print(sol.longestConsecutive([]))                          # 0
    print(sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))    # 7  (sequence: [-1,0,1])

"""
⏱ Time Complexity: O(n)
    - Each number is inserted into a set O(n).
    - Each number is checked and each sequence is traversed once overall.

💾 Space Complexity: O(n)
    - The hash set stores up to n elements.
"""
