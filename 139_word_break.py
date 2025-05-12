"""
🔷 LeetCode 139 – Word Break

🧠 Problem Summary:
Given a string `s` and a list of dictionary words `wordDict`, determine if `s` can be segmented 
into a space‑separated sequence of one or more dictionary words. You may reuse words.

✅ Constraints:
- 1 ≤ s.length ≤ 300  
- 1 ≤ wordDict.length ≤ 1000  
- 1 ≤ wordDict[i].length ≤ 20  
- All strings consist of lowercase English letters.  
- All words in wordDict are unique.  

---

📌 Examples:

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: True
Explanation: "leetcode" can be segmented as "leet code".


Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: True
Explanation: "applepenapple" = "apple pen apple".


Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: False
---

💡 Core Idea (DP):
Use a boolean DP array `dp` of size `n+1`, where `dp[i]` = True if `s[:i]` can be segmented.  
- Initialize `dp[0] = True` (empty string).  
- For each `i` from 1 to n, check each word in `wordDict`:  
  if `i >= len(word)` and `dp[i-len(word)]` is True and `s[i-len(word):i] == word`, set `dp[i] = True`.  

Return `dp[n]`.

---

👉 Follow‑up / Alternative (DFS + memo):
We can also perform a DFS trying to match dictionary words at each position, with memoization to avoid re‑visiting failed indices.  
This runs in O(n * m * L) worst‑case (n = len(s), m = |wordDict|, L = max word length), similar to DP.

"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        # dp[i] : can break s[:i]
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Precompute max word length to bound inner loop
        max_len = max((len(w) for w in wordDict), default=0)
        
        for i in range(1, n + 1):
            # Only need to check up to max_len characters back
            for l in range(1, min(i, max_len) + 1):
                if not dp[i - l]:
                    continue
                # If the substring s[i-l:i] is a dictionary word
                if s[i - l:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

    def wordBreak_dfs(self, s: str, wordDict: list[str]) -> bool:
        """Alternative DFS + memo solution."""
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        n = len(s)
        memo = {}

        def dfs(start: int) -> bool:
            if start == n:
                return True
            if start in memo:
                return memo[start]
            # try all word lengths up to max_len
            for l in range(1, min(n - start, max_len) + 1):
                if s[start:start + l] in word_set and dfs(start + l):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)


# -------------------------
# 🔸 Example test runs
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("leetcode", ["leet","code"], True),
        ("applepenapple", ["apple","pen"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False),
    ]
    for s, wd, ans in tests:
        print(s, sol.wordBreak(s, wd), "expected", ans)
        print(s, sol.wordBreak_dfs(s, wd), "expected", ans)
        print("----")

"""
⏱ Time Complexity:
- DP solution: O(n * L) where n = len(s), L = total length checked per position (bounded by max word length).
- DFS+memo: O(n * L) as well in the worst case.

💾 Space Complexity:
- DP: O(n)
- DFS+memo: O(n) for recursion/memo.
"""
