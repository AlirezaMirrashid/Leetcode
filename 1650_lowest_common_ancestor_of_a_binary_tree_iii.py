"""
LeetCode 1650 - Lowest Common Ancestor of a Binary Tree III 
Description
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        
        # Traverse up from both nodes
        while p or q:
            if p:
                if p in seen:
                    return p
                seen.add(p)
                p = p.parent

            if q:
                if q in seen:
                    return q
                seen.add(q)
                q = q.parent
        
        return None  # Shouldn't happen if p and q are guaranteed to be in the tree

    def lowestCommonAncestorConstantSpace(self, p: 'Node', q: 'Node') -> 'Node':
        """
        ✅ Constant-Space Depth Alignment Approach

        1. Compute depth of p and q by walking up to root.
        2. Advance the deeper node up by the depth difference.
        3. Move both p and q up together until they meet.

        ⏱ Time Complexity: O(h) where h is tree height  
        💾 Space Complexity: O(1)  
        """
        # 1) compute depths
        dp, dq = 0, 0
        a, b = p, q
        while a:
            dp += 1
            a = a.parent
        while b:
            dq += 1
            b = b.parent

        # 2) align depths
        if dp > dq:
            for _ in range(dp - dq):
                p = p.parent
        else:
            for _ in range(dq - dp):
                q = q.parent

        # 3) ascend together
        while p is not q:
            p = p.parent
            q = q.parent

        return p
