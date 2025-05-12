"""
🔵 LeetCode 138: Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could 
point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new 
node has its value set to the value of its corresponding original node. Both the next and random pointer of 
the new nodes should point to new nodes in the copied list such that the pointers in the original list and 
copied list represent the same list state. None of the pointers in the new list should point to nodes in the 
original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the 
corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

-----------------------------------
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Explanation: 
    The deep copy of the list is created such that each new node has the same value as its corresponding 
    original node, and the next and random pointers are set accordingly.

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Explanation:
    The deep copy is created, where for each node in the original list, the random pointer of the new node 
    points to the new copy of the node pointed to by the original random pointer.

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

-----------------------------------
Constraints:
    - 0 <= n <= 1000
    - -10^4 <= Node.val <= 10^4
    - Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional

class Node:
    def __init__(self, val: int = 0, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    """
    Creates a deep copy of a linked list with a random pointer.
    
    Approach:
      - Use a dictionary to map each original node to its copied node.
      - First pass: Create all new nodes with the same value as the original nodes and store the mapping.
      - Second pass: Assign the next and random pointers for the copied nodes using the mapping.
    
    Time Complexity: O(n), where n is the number of nodes in the original list.
    Space Complexity: O(n), for the dictionary mapping original nodes to their copies.
    
    Args:
        head (Optional[Node]): The head of the original linked list.
    
    Returns:
        Optional[Node]: The head of the deep-copied linked list.
    """
    if not head:
        return None

    # Dictionary to hold mapping from original nodes to their copies.
    node_map = {}
    
    # First pass: Create new nodes for each original node.
    current = head
    while current:
        node_map[current] = Node(current.val)
        current = current.next

    # Second pass: Assign next and random pointers for the new nodes.
    current = head
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        else:
            node_map[current].next = None
        
        if current.random:
            node_map[current].random = node_map[current.random]
        else:
            node_map[current].random = None
        
        current = current.next

    return node_map[head]

# Helper function to print the list for testing purposes.
def printList(head: Optional[Node]) -> None:
    """
    Prints the linked list nodes along with their random pointer values.
    Each node is printed as: Node(val, random_val) where random_val is the value of the random node or None.
    """
    current = head
    result = []
    while current:
        random_val = current.random.val if current.random else None
        result.append(f"({current.val}, {random_val})")
        current = current.next
    print(" -> ".join(result))

# Sample Test Cases
if __name__ == "__main__":
    # Constructing Example 1:
    # Original list: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    node0 = Node(7)
    node1 = Node(13)
    node2 = Node(11)
    node3 = Node(10)
    node4 = Node(1)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Setting up random pointers according to the example:
    node0.random = None
    node1.random = node0
    node2.random = node4
    node3.random = node2
    node4.random = node0

    # Create a deep copy of the list
    copied_head = copyRandomList(node0)

    # Print original and copied lists to verify deep copy
    print("Original list:")
    printList(node0)
    print("\nCopied list:")
    printList(copied_head)

# ------------------------------------------------
# ✅ Time Complexity: O(n), where n is the number of nodes in the linked list.
# ✅ Space Complexity: O(n), due to the dictionary used for mapping.
