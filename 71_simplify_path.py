"""
🔷 LeetCode 71 - Simplify Path

🧠 Task:
Given an absolute Unix-style path, return its simplified canonical path.
Rules:
- "." means current dir → skip
- ".." means go up → pop last dir
- "//" or multiple slashes → treated as "/"
- Other entries are valid directory/file names

📁 The path must:
- Start with a single slash "/"
- Have no trailing slash (unless it's root)
- Not contain "." or ".."
"""
from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        ✅ Stack-based parsing of path components.

        ⏱ Time Complexity: O(n) — where n is the length of the path
        💾 Space Complexity: O(n) — stack holds at most all path components
        """
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


# 🔸 Sample test runs
if __name__ == "__main__":
    sol = Solution()
    test_paths = [
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
        "/.../a/../b/c/../d/./"
    ]

    for path in test_paths:
        print("Input:", path)
        print("Output:", sol.simplifyPath(path))
        print("------------")
