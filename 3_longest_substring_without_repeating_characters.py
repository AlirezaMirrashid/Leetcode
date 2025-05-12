"""
🔷 LeetCode 3 – Longest Substring Without Repeating Characters

🧠 Problem Summary:
Given a string `s`, return the length of the longest substring without repeating characters.

✅ Constraints:
- 0 ≤ s.length ≤ 5 × 10⁴
- s consists of English letters, digits, symbols, spaces

---

📌 Example:

Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3 ("wke")

---

💡 Solution 1 (Sliding Window with Set):
- Use two pointers and a set to track unique characters.
- Expand right pointer, if duplicate found → shrink left pointer.

💡 Solution 2 (Optimized Sliding Window with Dict):
- Use a dictionary to store last index of each character.
- Jump the left pointer to `dict[char] + 1` if duplicate found.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

    def lengthOfLongestSubstringOptimized(self, s: str) -> int:
        char_index = {}
        left = max_len = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))      # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))        # 1
    print(sol.lengthOfLongestSubstring("pwwkew"))       # 3
    print(sol.lengthOfLongestSubstringOptimized("abcabcbb")) # 3

"""
⏱ Time Complexity:
- Both solutions: O(n)

💾 Space Complexity:
- Set version: O(min(n, m)) where m is the charset size
- Optimized dict version: O(min(n, m))
"""
