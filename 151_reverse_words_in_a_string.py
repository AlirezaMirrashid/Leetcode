"""
🔷 LeetCode 151 – Reverse Words in a String

🧠 Problem Summary:
Given a string `s`, reverse the order of words. A word is defined as a sequence of non-space characters.
Multiple spaces between words should be reduced to one, and leading/trailing spaces should be removed.

---

💡 Alternate Solution (From Scratch):
- Traverse the string manually.
- Extract words while skipping multiple spaces.
- Reverse the list of words.
- Join them with a single space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        words = []

        # Manual splitting, skipping spaces
        while i < n:
            # Skip leading spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break

            # Build the word
            j = i
            while j < n and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j

        # Reverse and join with single space
        return ' '.join(reversed(words))


# 🔸 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))        # "blue is sky the"
    print(sol.reverseWords("  hello world  "))        # "world hello"
    print(sol.reverseWords("a good   example"))       # "example good a"
    print(sol.reverseWords("   singleWord   "))       # "singleWord"
    print(sol.reverseWords(" multiple    spaces "))   # "spaces multiple"

"""
⏱ Time Complexity: O(n)
    - One full traversal to parse the words, one reverse, one join.

💾 Space Complexity: O(n)
    - To store the list of words and final string.
"""
