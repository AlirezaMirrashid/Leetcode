"""
🔷 LeetCode 339 - Nested List Weight Sum

🧠 Task:
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
Each element is either an integer or a list of elements, which may themselves be integers or other lists.

Example 1:
Input: [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1 → 4*2 + 2*1 = 10.

Example 2:
Input: [1,[4,[6]]]
Output: 27
Explanation: 1*1 + 4*2 + 6*3 = 27.

Constraints:
- The total number of nested elements does not exceed 10^4.
- Depth does not exceed 1000.
"""

from collections import deque
from typing import List, Union

# Provided interface for nested integer
class NestedInteger:
    def isInteger(self) -> bool:
        ...
    def getInteger(self) -> int:
        ...
    def getList(self) -> List['NestedInteger']:
        ...

class Solution:
    def depthSumDFS(self, nestedList: List[NestedInteger]) -> int:
        """
        ✅ DFS Recursion

        Traverse recursively, carrying current depth. Sum integer * depth.

        Time Complexity: O(N) where N is total elements
        Space Complexity: O(D) recursion depth (D = max depth)
        """
        def dfs(nest: NestedInteger, depth: int) -> int:
            if nest.isInteger():
                return nest.getInteger() * depth
            total = 0
            for ni in nest.getList():
                total += dfs(ni, depth + 1)
            return total

        total_sum = 0
        for ni in nestedList:
            total_sum += dfs(ni, 1)
        return total_sum

    def depthSumBFS(self, nestedList: List[NestedInteger]) -> int:
        """
        ✅ BFS Level-Order

        Use a queue of (NestedInteger, depth). Process breadth-first.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        total_sum = 0
        queue = deque((ni, 1) for ni in nestedList)
        while queue:
            ni, depth = queue.popleft()
            if ni.isInteger():
                total_sum += ni.getInteger() * depth
            else:
                for child in ni.getList():
                    queue.append((child, depth + 1))
        return total_sum

# ------------ Sample usage ------------
if __name__ == "__main__":
    # We cannot run without actual NestedInteger implementation, but conceptually:
    # Example 1: [[1,1],2,[1,1]] → 10
    # Example 2: [1,[4,[6]]] → 27
    pass
