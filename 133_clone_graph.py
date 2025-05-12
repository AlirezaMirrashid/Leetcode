"""
🔷 LeetCode 133 - Clone Graph

🧠 Task:
Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node contains a value and a list of its neighbors.

Use 1-indexed node values; the given node has val = 1.

-----------------------------------
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Example 2:
Input: adjList = [[]]
Output: [[]]

Example 3:
Input: adjList = []
Output: []

-----------------------------------
Constraints:
- Number of nodes in [0,100]
- Node.val unique in [1,100]
- No self-loops or duplicate edges
- Graph is connected (if non-empty)

"""
from collections import deque
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraphDFS(self, node: 'Node') -> 'Node':
        """
        ✅ DFS Recursion + HashMap

        Use a dictionary to map original nodes to their clones. Recursively clone neighbors.

        ⏱ Time Complexity: O(N + E)
        💾 Space Complexity: O(N) for recursion stack and map
        """
        old_to_new = {}
        
        def dfs(n: 'Node') -> 'Node':
            if n in old_to_new:
                return old_to_new[n]
            clone = Node(n.val)
            old_to_new[n] = clone
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node) if node else None

    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        """
        ✅ BFS + HashMap

        Iteratively traverse using queue. For each original node, create clone and enqueue neighbors.

        ⏱ Time Complexity: O(N + E)
        💾 Space Complexity: O(N)
        """
        if not node:
            return None
        old_to_new = {node: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])
        return old_to_new[node]

    def cloneGraphBrute(self, node: 'Node') -> 'Node':
        """
        ❌ Brute Force: Serialize & Rebuild

        1. BFS to capture adjacency list in array form.
        2. Build fresh Node objects from adjacency data.

        ⏱ Time Complexity: O(N + E)
        💾 Space Complexity: O(N + E)
        """
        if not node:
            return None
        # 1. serialize
        q = deque([node])
        visited = {node}
        adj = {node.val: []}
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                adj[cur.val].append(nei.val)
                if nei not in visited:
                    visited.add(nei)
                    adj[nei.val] = []
                    q.append(nei)
        # 2. rebuild
        clones = {val: Node(val) for val in adj}
        for val, neigh_list in adj.items():
            clones[val].neighbors = [clones[nv] for nv in neigh_list]
        return clones[node.val]

# Note: to test, build Node graph from adjacency list, then run cloneGraph...
