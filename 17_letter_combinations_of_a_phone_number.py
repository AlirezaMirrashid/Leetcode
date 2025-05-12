"""
🔷 LeetCode 17 – Letter Combinations of a Phone Number

🧠 Problem Summary:
Given a string `digits` containing digits from 2–9 inclusive, return all possible letter
combinations that the number could represent, using the classic telephone button mapping.
Return the answer in any order. If `digits` is empty, return an empty list.

✅ Constraints:
- 0 ≤ digits.length ≤ 4  
- digits[i] is a digit in the range ['2', '9']  

---

📌 Examples:

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]



---

💡 Core Idea:
This is a classic backtracking (DFS) or BFS problem over a small branching factor (at most 4 letters per digit)
and depth up to 4. Build combinations by appending each possible letter for the next digit.

We provide two approaches:
1. DFS Backtracking
2. BFS Iterative (queue-based)

"""

from collections import deque

class Solution:
    # mapping from digit to letters
    _map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> list[str]:
        """DFS backtracking solution."""
        if not digits:
            return []
        ans = []
        n = len(digits)

        def dfs(idx: int, path: list[str]):
            if idx == n:
                ans.append("".join(path))
                return
            letters = Solution._map[digits[idx]]
            for ch in letters:
                path.append(ch)
                dfs(idx + 1, path)
                path.pop()

        dfs(0, [])
        return ans

    def letterCombinations_bfs(self, digits: str) -> list[str]:
        """BFS iterative solution using a queue."""
        if not digits:
            return []
        queue = deque([""])
        for d in digits:
            letters = Solution._map[d]
            # For each existing partial combination, extend by each letter
            for _ in range(len(queue)):
                prev = queue.popleft()
                for ch in letters:
                    queue.append(prev + ch)
        return list(queue)


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
    ]
    for digits, expected in tests:
        res1 = sol.letterCombinations(digits)
        res2 = sol.letterCombinations_bfs(digits)
        print(f"DFS {digits!r} -> {res1}, expected {expected}")
        print(f"BFS {digits!r} -> {res2}, expected {expected}")
        print("----")

"""
⏱ Time Complexity:
- DFS: O(4^n · n) where n = len(digits), since each position branches up to 4 ways and building each string costs O(n).
- BFS: O(4^n · n) similarly, as we generate all combinations and each string concatenation is O(n).

💾 Space Complexity:
- O(4^n · n) to store all combinations in the output, plus O(n) recursion stack for DFS or O(4^n · n) queue for BFS.
"""






